import warnings
from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.secret_key = 'sessionData'

app.config['TESTING'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_RECORD_QUERIES'] = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ihdrdjsbbqcgfd:42fea0b1fac86013911e6e70f91c80121b9ab8b15abba29b5b3a31bf78d2a028@ec2-3-224-164-189.compute-1.amazonaws.com:5432/d316qc0c5o2i1m'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=25)

#app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

app.config['DEBUG'] = True

db = SQLAlchemy(app)

import project.com.controller
