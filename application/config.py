import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Base configuration"""

class ProductionConfig(Config):
    """Production configuration"""
    PRODUCTION = True 

class DevelopmentConfig(Config):
    """Development configuration""" 

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True          