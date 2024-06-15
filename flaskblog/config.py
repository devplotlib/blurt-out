import os

class Config:
    SECRET_KEY = 'asdasdawd123131313wefusdfwer23402'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_PASSWORD = 'fsvj ohhl toqu tdeq'
    MAIL_USERNAME = os.environ.get('TEST_EMAIL')
