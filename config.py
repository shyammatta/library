import os
from urllib.parse import quote_plus
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisisarandomgeneratedstring'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:{}@localhost:3306/book_management12".format(quote_plus("system"))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
