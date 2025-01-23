import os

class Config:
    # Database settings
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Thought%401234@localhost/mobile_store'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Other optional settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')  # Secret key for sessions and security
    DEBUG = True  # Enable debugging during development


