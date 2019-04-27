from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project2:june1997@localhost/project2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gkyzmbizacxrmw:75966ee0b33296949eb5fe93522abf4b35b570bb949101e3d6a163c6b4217f0f@ec2-50-17-246-114.compute-1.amazonaws.com:5432/dudgtvsqgan12'

app.config['UPLOAD_FOLDER']='./app/static/uploads'


db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
app.debug= True
from app import views