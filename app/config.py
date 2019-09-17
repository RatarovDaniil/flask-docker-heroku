import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
