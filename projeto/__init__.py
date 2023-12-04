from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'FFTYGVBT65R556DTRD6T78FFF87FG78F6F6F6CCV8G7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['MIME_TYPES'] = {
    'mp4': 'video/mp4',
    'webm': 'video/webm',
}

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por Favor, Faça login ou crie uma conta para acessar essa página!'
login_manager.login_message_category = 'alert-info'

from projeto import routes
