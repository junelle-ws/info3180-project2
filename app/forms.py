from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import DateField
from datetime import date

class Register(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    bio = StringField('Biography', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!']) ])


class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])



class Post(FlaskForm):
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!']) ])
    caption = password = StringField('Caption', validators=[DataRequired()])
    created_on = DateField("Start date", default=date.today(), format='%d/%m/%Y', validators=[DataRequired(message="You need to enter the date created")],)
    
    
    
    
    