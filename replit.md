# SolveXtra - Professional Quality Solutions Website

## Overview
A modern, interactive landing page for SolveXtra, a company providing professional quality audits and customer experience solutions. The website features an elegant dark theme with gradient accents, 3D background effects, and interactive card stacking.

## Tech Stack
- **Frontend**: Static HTML with vanilla JavaScript
- **Styling**: Tailwind CSS (CDN)
- **Icons**: Lucide Icons
- **3D Graphics**: Three.js, Spline 3D viewer
- **Server**: Python HTTP server

## Project Structure
```
/
├── index.html           # Main landing page
├── server.py           # Python HTTP server
└── replit.md          # Project documentation
```

## Features
- Interactive card stack showcasing three service offerings
- Animated fade-in effects for content
- 3D background with neural network visualization
- Responsive design
- Success stories and testimonials sections
- Modern glass-morphism UI elements

## Running the Project
The project is configured to run automatically via the workflow system:
- Server runs on port 5000
- Accessible via the Replit webview

## Services Showcased
1. **Quality Audits** - Human-centric quality management with 100% audit accuracy
2. **CX Audits** - End-to-end customer experience optimization (+35% CSAT improvement)
3. **Consulting Services** - Strategic advisory and digital transformation (+58% process efficiency)

## Recent Changes
- **2025-10-05**: Prepared for Railway deployment
  - Added Procfile, railway.json, runtime.txt, requirements.txt
  - Updated server.py to support both Replit and Railway PORT configuration
  - Modified SendGrid integration to support direct env vars for Railway
  - Created README_RAILWAY.md with deployment instructions
  - Updated "Get Demo" button to scroll to contact form
- **2025-10-05**: Integrated SendGrid email API for contact form
  - Connected SendGrid integration via Replit connectors
  - Created /api/contact endpoint to handle form submissions
  - Contact form now sends emails to contactus@solvextra.com
  - Added success/error feedback messages to form
  - Updated testimonial job titles to reflect actual client positions
- **2025-10-05**: Updated branding and color scheme
  - Replaced logo with custom cyan/blue gradient logo (increased to 12x12px)
  - Updated all color gradients from orange/pink to cyan/blue theme
  - Updated buttons, progress bars, and accent colors to match new branding
- **2025-10-05**: Initial setup in Replit environment
  - Renamed HTML file to index.html
  - Created Python HTTP server with cache control headers
  - Configured workflow for port 5000
  - Added .gitignore for Python files

## Deployment
The project is ready to deploy on Railway. See README_RAILWAY.md for deployment instructions.
