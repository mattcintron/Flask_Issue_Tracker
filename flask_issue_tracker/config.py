import os

class Config:
    SECRET_KEY = 'kiah7tsytdfra54sr987yau512wa'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # email vars
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'bioinformaticsmanager@gmail.com'
    MAIL_PASSWORD = 'ty56ty56'