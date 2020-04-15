import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

config = {"SQLALCHEMY_DATABASE_URI" : "postgresql:///nlp_user:Welcome@123@localhost/nlp",
		  'SQLALCHEMY_TRACK_MODIFICATIONS' : True,
		  'DEBUG' : False,
		  'SECRET_KEY' : os.urandom(32),
		  #'APPLICATION_ROOT' : os.path.,
		  'PREFERRED_URL_SCHEME' : 'https',
		  'JSON_AS_ASCII' : True,
		  'JSON_SORT_KEYS' : True,
		  'SESSION_COOKIE_NAME' : 'thepandelivery_session',
		  }


application = Flask(__name__)
db = SQLAlchemy(application)

# Word models
from web_app import models

db.create_all()
migrate = Migrate(application, db)

 
