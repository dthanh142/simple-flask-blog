import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thanh0412'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 5
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    
    # LANGUAGES = ['en', 'es']
    LANGUAGES = ['vi', 'en', 'es']

    # translator
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

    # mail config
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['t.clone.214@gmail.com']

    # $env:MAIL_PORT=587
    # $env:MAIL_USE_TLS=1
    # $env:MAIL_USERNAME="t.clone.214@gmail.com"
    # $env:MAIL_PASSWORD="thanh0412"
    # $env:MAIL_SERVER="smtp.googlemail.com"