import logging
import os

from datetime import datetime, timedelta
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_jwt_extended import JWTManager

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
print('BASE_DIR', BASE_DIR)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
logging.basicConfig(filename='flask-tailwind-initial.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app.config['SECRET_KEY'] = 'changethis_BDy9asydnasdna98n^B&D*tsa87dvbats67asrv67r'

# POSTGRES = {
#     'user': 'uer',
#     'pw': 'password',
#     'db': 'db_name',
#     'host': 'db_host',
#     'port': 'db_port',
# }
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-tailwind-initial.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "changethis_s0m37h1ng53cr37**&SA*&%^&*%*^*("
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1440)
app.config["JWT_ERROR_MESSAGE_KEY"] = "Error"

jwt = JWTManager(app)

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'

from core import routes, views, api_user

# pip install Flask-SQLAlchemy
