# Medical Records App - README

## Overview

This application provides a secure interface for medical records staff to access and download daily patient data from emergency department visits. The system dynamically captures data from a Google Sheet, retains it for 1 week with automatic deletion, and restricts access to authorized personnel only.

## Features

- **Secure Authentication**: Role-based access control for Medical Records staff and administrators
- **Dynamic Data Capture**: Automatically retrieves the latest data from Google Sheets
- **Data Retention Policy**: 7-day data retention with automatic deletion
- **Responsive Interface**: Works on desktop and mobile devices
- **Export Options**: Download data in various formats with filtering capabilities

## Directory Structure

```
medical_records_app/
├── frontend/               # Frontend static files
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   └── index.html          # Main HTML file
├── backend/                # Backend Python code
│   ├── api/                # API endpoints
│   ├── auth/               # Authentication system
│   └── utils/              # Utility functions
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── Procfile                # For deployment
├── DEPLOYMENT.md           # Deployment instructions
└── README.md               # This file
```

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Authentication**: JWT (JSON Web Tokens)
- **Data Source**: Google Sheets API
- **Deployment**: Gunicorn, Nginx/Apache

## Getting Started

See the [DEPLOYMENT.md](DEPLOYMENT.md) file for detailed instructions on how to deploy this application.

## Default Users

The application comes with two default user roles:

1. **Medical Records Staff**
   - Username: `medical_records`
   - Password: `medical123`
   - Access: View and download patient data

2. **Administrator**
   - Username: `admin`
   - Password: `admin123`
   - Access: All features plus administrative functions

**Important**: Change these default passwords before deploying to production!

## Data Security

- All patient data is accessed securely through the Google Sheets API
- Data is retained for only 7 days to comply with data minimization principles
- Authentication is required for all data access
- Role-based permissions restrict access to authorized personnel only

## Customization

The application can be customized in several ways:

- Modify the frontend CSS to match your organization's branding
- Add additional user roles in the authentication system
- Adjust the data retention period in the configuration
- Extend the API to include additional data sources

## Support

For questions or issues, please refer to the deployment documentation or contact your system administrator.
