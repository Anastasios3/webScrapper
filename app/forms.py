from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from email_validator import validate_email, EmailNotValidError

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')

class ExportForm(FlaskForm):
    submit = SubmitField('Export Tasks')
