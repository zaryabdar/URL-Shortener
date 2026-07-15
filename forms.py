from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, URLField
from wtforms.validators import DataRequired, Email, Length, EqualTo,URL

class RegistrationForm(FlaskForm):
    username =StringField("Username", validators=[DataRequired(),Length(min=5, max=20)])
    email =StringField("Email", validators=[DataRequired(),Email()])
    password =PasswordField("Password", validators=[DataRequired(),Length(min=8, max=20)])
    confirm_password =PasswordField("Confirm Password", validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email =StringField("Email", validators=[DataRequired(),Email()])
    password =PasswordField("Password", validators=[DataRequired(),Length(min=8, max=20)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class UrlForm(FlaskForm):
    original_url = URLField("Enter URL", validators=[DataRequired(),URL()])
    submit = SubmitField("Shorten")

