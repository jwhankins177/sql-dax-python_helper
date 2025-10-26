"""Initialize the Flask application."""
from flask import Flask
from config import config


def create_app(config_name='default'):
    """Create and configure the Flask application.
    
    Args:
        config_name: The configuration to use (development, production, testing, or default)
        
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app
