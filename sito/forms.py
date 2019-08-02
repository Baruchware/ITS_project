from flask_wtf import FlaskForm #possibilità di fare form in python 
from wtforms import BooleanField,PasswordField,StringField,SubmitField #importo i campi che necessito per il login
from wtforms.validators import DataRequired #importo validatore


class LoginForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()]) #crei campi, nella stringa c'è l outpput all utente per sapere cosa digitare
    password=PasswordField('Password', validators=[DataRequired()]) #e validators=[DataRequired()] indica che il dato
    remember_me = BooleanField('Ricorda i dati di accesso') #è necessario per il login
    submit = SubmitField('Login')
