from flask import Flask, Blueprint, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os

# Import configuration
from backend.config import SECRET_KEY, JWT_SECRET_KEY, JWT_ACCESS_TOKEN_EXPIRES

def create_app():
    """Create and configure the Flask application"""
    # Create Flask app
    app = Flask(__name__, static_folder='frontend')
    
    # Configure app
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
    
    # Enable CORS
    CORS(app)
    
    # Initialize JWT
    jwt = JWTManager(app)
    
    # Import routes here to avoid circular imports
    from backend.auth.routes import auth_routes
    from backend.api.routes import api_routes
    from backend.utils.retention_routes import retention_routes
    
    # Register blueprints
    app.register_blueprint(auth_routes, url_prefix='/api')
    app.register_blueprint(api_routes, url_prefix='/api')
    app.register_blueprint(retention_routes, url_prefix='/api/retention')
    
    # Serve frontend files
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_frontend(path):
        if path == '':
            return send_from_directory('frontend', 'index.html')
        try:
            return send_from_directory('frontend', path)
        except:
            return send_from_directory('frontend', 'index.html')
    
    return app

# Create app instance
app = create_app()
