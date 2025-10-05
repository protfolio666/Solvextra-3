# Railway Deployment Guide

## Quick Deploy to Railway

1. **Connect your GitHub repository to Railway:**
   - Go to [railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select this repository

2. **Configure Environment Variables:**
   - In Railway dashboard, go to your project
   - Navigate to "Variables" tab
   - Add the following variables:
     - `REPLIT_CONNECTORS_HOSTNAME` - (Your SendGrid connector hostname)
     - `REPL_IDENTITY` or `WEB_REPL_RENEWAL` - (Your authentication token)
   
   **Note:** For SendGrid to work on Railway, you'll need to configure SendGrid API credentials directly:
   - `SENDGRID_API_KEY` - Your SendGrid API key
   - `SENDGRID_FROM_EMAIL` - Your verified sender email

3. **Deploy:**
   - Railway will automatically detect the configuration files
   - The app will build and deploy automatically
   - Your app will be available at the Railway-provided URL

## Files for Railway Deployment

- `Procfile` - Tells Railway how to start the app
- `railway.json` - Railway-specific configuration
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification
- `server.py` - Main application (configured to use Railway's PORT env var)

## Testing Locally

```bash
python server.py
```

The server will run on port 5000 locally, or use Railway's PORT in production.
