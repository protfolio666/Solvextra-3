import http.server
import socketserver
import os
import json
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from urllib.parse import parse_qs

PORT = int(os.environ.get('PORT', 5000))
HOST = "0.0.0.0"

def get_sendgrid_credentials():
    api_key = os.environ.get('SENDGRID_API_KEY')
    from_email = os.environ.get('SENDGRID_FROM_EMAIL')
    
    if api_key and from_email:
        return {'api_key': api_key, 'from_email': from_email}
    
    hostname = os.environ.get('REPLIT_CONNECTORS_HOSTNAME')
    x_replit_token = None
    
    if os.environ.get('REPL_IDENTITY'):
        x_replit_token = 'repl ' + os.environ.get('REPL_IDENTITY')
    elif os.environ.get('WEB_REPL_RENEWAL'):
        x_replit_token = 'depl ' + os.environ.get('WEB_REPL_RENEWAL')
    
    if not x_replit_token:
        raise Exception('SendGrid credentials not configured. Please set SENDGRID_API_KEY and SENDGRID_FROM_EMAIL environment variables.')
    
    url = f'https://{hostname}/api/v2/connection?include_secrets=true&connector_names=sendgrid'
    headers = {
        'Accept': 'application/json',
        'X_REPLIT_TOKEN': x_replit_token
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if not data.get('items') or len(data['items']) == 0:
        raise Exception('SendGrid not connected')
    
    settings = data['items'][0].get('settings', {})
    api_key = settings.get('api_key')
    from_email = settings.get('from_email')
    
    if not api_key or not from_email:
        raise Exception('SendGrid credentials not found')
    
    return {'api_key': api_key, 'from_email': from_email}

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def do_POST(self):
        if self.path == '/api/contact':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))
                
                credentials = get_sendgrid_credentials()
                
                message = Mail(
                    from_email=credentials['from_email'],
                    to_emails='contactus@solvextra.com',
                    subject=f"New Contact Form: {data.get('subject', 'General Inquiry')}",
                    html_content=f"""
                    <h2>New Contact Form Submission</h2>
                    <p><strong>Name:</strong> {data.get('name', 'N/A')}</p>
                    <p><strong>Email:</strong> {data.get('email', 'N/A')}</p>
                    <p><strong>Company:</strong> {data.get('company', 'N/A')}</p>
                    <p><strong>Phone:</strong> {data.get('phone', 'N/A')}</p>
                    <p><strong>Subject:</strong> {data.get('subject', 'N/A')}</p>
                    <p><strong>Message:</strong></p>
                    <p>{data.get('message', 'N/A')}</p>
                    <p><strong>Newsletter Subscription:</strong> {'Yes' if data.get('newsletter') else 'No'}</p>
                    """
                )
                
                sg = SendGridAPIClient(credentials['api_key'])
                response = sg.send(message)
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True, 'message': 'Email sent successfully'}).encode())
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer((HOST, PORT), MyHTTPRequestHandler) as httpd:
    print(f"Server running at http://{HOST}:{PORT}/")
    httpd.serve_forever()
