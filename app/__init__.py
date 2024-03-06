from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
import os
# import flask migrate here
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')
db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate = Migrate(app, db) 

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views
