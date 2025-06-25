import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # MUST be set on Render
    SQLALCHEMY_TRACK_MODIFICATIONS = False
