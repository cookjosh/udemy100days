from tokenize import String
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField
from wtforms.validators import InputRequired, Length
from werkzeug.utils import secure_filename

class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')