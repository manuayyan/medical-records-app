# Medical Records Application Deployment Guide

This document provides instructions for deploying the complete Medical Records Application, including both frontend and backend components.

## Overview

The Medical Records Application is designed to:
- Access and download daily patient data from emergency department visits
- Dynamically capture data from Google Sheets
- Retain data for 1 week with automatic deletion
- Provide secure access for Medical Records staff and administrators

## System Requirements

- Python 3.8 or higher
- Node.js 14 or higher (for development only)
- Web server (Apache or Nginx)
- HTTPS certificate for production deployment
- Google Cloud Platform account for Google Sheets API

## Deployment Steps

### 1. Set Up Google Sheets API

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Sheets API
4. Create credentials (Service Account)
5. Download the JSON key file
6. Share your Google Sheet with the service account email address (with editor permissions)

### 2. Configure Backend

1. Copy the Google API credentials JSON file to `/path/to/app/backend/credentials.json`
2. Create a `.env` file in the root directory with the following variables:

```
SECRET_KEY=your_secret_key_here
JWT_SECRET_KEY=your_jwt_secret_key_here
GOOGLE_SHEET_ID=1Sb_WJkMHypFwx7lRfO65tIS8Z8Qo_TLpmYJPzghKNjc
DATA_RETENTION_DAYS=7
```

Replace `your_secret_key_here` and `your_jwt_secret_key_here` with secure random strings.

### 3. Install Dependencies

```bash
# Install backend dependencies
pip install -r requirements.txt
```

### 4. Configure User Authentication

Edit the user database in `/backend/auth/routes.py` to add your organization's users:

```python
users = {
    'medical_records': {
        'password': 'secure_password_here',
        'role': 'medical_records'
    },
    'admin': {
        'password': 'secure_admin_password_here',
        'role': 'admin'
    }
    # Add more users as needed
}
```

For production, consider implementing a more secure authentication system with password hashing.

### 5. Deploy the Application

#### Option A: Deploy with Gunicorn (Recommended for Production)

1. Install Gunicorn:
```bash
pip install gunicorn
```

2. Start the application:
```bash
gunicorn --bind 0.0.0.0:8080 app:app
```

3. Configure a web server (Nginx or Apache) as a reverse proxy to the Gunicorn server

#### Option B: Deploy with Flask Development Server (For Testing Only)

```bash
python app.py
```

### 6. Configure Web Server (Nginx Example)

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    # Redirect HTTP to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;
    
    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 7. Set Up Data Retention Cron Job

Create a cron job to run the data retention script daily:

```bash
# Add to crontab
0 0 * * * /usr/bin/python3 /path/to/app/backend/utils/run_retention.py
```

## Testing the Deployment

1. Access the application at your domain
2. Log in with the credentials you configured:
   - Medical Records: username `medical_records`, password as configured
   - Admin: username `admin`, password as configured
3. Verify that you can view and download patient data
4. Test the data retention policy by checking that records older than 7 days are not available

## Troubleshooting

### Common Issues

1. **Google Sheets API Connection Errors**
   - Verify that the credentials.json file is correctly placed
   - Ensure the Google Sheet is shared with the service account
   - Check that the GOOGLE_SHEET_ID in .env matches your sheet

2. **Authentication Issues**
   - Verify JWT_SECRET_KEY is set correctly
   - Check user credentials in the routes.py file

3. **Data Not Displaying**
   - Check browser console for JavaScript errors
   - Verify API endpoints are accessible
   - Ensure Google Sheet has the expected format

### Logs

- Application logs: Check the output of the Gunicorn or Flask process
- Data retention logs: `/logs/retention_log.txt`

## Security Considerations

1. Always use HTTPS in production
2. Regularly update the passwords in the user database
3. Consider implementing a more robust authentication system for production
4. Restrict access to the server to authorized personnel only
5. Regularly back up your Google Sheet data

## Support

For additional support, please contact the development team.
