"""Configuration settings for the SQL-DAX-Python Helper application."""
import os


class Config:
    """Base configuration class."""
    
    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Application settings
    DEBUG = False
    TESTING = False
    
    # Flask settings
    HOST = '127.0.0.1'
    PORT = 5000


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    HOST = '0.0.0.0'  # Bind to all interfaces in production


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
