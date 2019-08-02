from datetime import datetime
from flask_login import UserMixin   #Se analizziamo UserMixin vediamo che ci sono funzione come is_authenticated , is_active, is_anonymous, get_id ecc...


from werkzeug.security import check_password_hash, generate_password_hash   # librerie crittografia password
from sito import db, loginmanager   #importo istanze create in __init__.py



@loginmanager.user_loader #attenzione che il decoratore in questo caso "loginmanager" deve essere la variabile loginmanager dichiarata prima in __init__.py
def load_user(id):
    return User.query.get(int(id))  #serve per tenere traccia dell utente connesso

#Aggiungiamo quindi UserMixin alla classe User per poter ottenere la possibilità di usare funzioni riguardante istanze in questa tabella

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)#creo una colonna nel database che supporti il tipo INTERO, ed evenutali altri parametri con prymary key
    created_at = db.Column(db.DateTime, default=datetime.now)#creo colonna che riporti la data e il momento in cui si creera questa istanza
    username = db.Column(db.String(12), unique=True, nullable=False ) #stringhe, con non piu di 12 caratteri, non puo essere nullo, e deve un username univoco
    email = db.Column(db.String(50), unique=True, nullable=False ) #colonna tipo stringa, 50 caratteri max, anche qui univoca, e dev esserci perforza
    password = db.Column(db.String(250), nullable = False) #colonna stringa, max 250, deve esserci perforza, per critto vedremo poi


    def __repr__(self):
        return (f"User('{self.id}, {self.created_at}, { self.username}, {self.email}, {self.password}") #senza questa funzione, se interroghiamo
    #il database chiedendogli un istanza generale come User.query.first() ci risponderà per esempio : <User 1>, invece ora otteniamo un output desiderato.

    def set_password_hash(self, password):
        self.password = generate_password_hash(password) #hashing delle password, serve cosi a poterle camuffare

    def check_password(self, password):
        return check_password_hash(self.password, password) #nonostante la crittografia con questo metodo puoi ottenere True se la password è corretta


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)#creo colonna che riporti la data e il momento in cui si creera questa istanza
    temperatura = db.Column(db.Integer, nullable=False)
    mode = db.Column(db.String, nullable = False)
    stato = db.Column(
    db.String, nullable = False)

    def __repr__(self):
        return (f"Info({self.id}, {self.created_at}, { self.temperatura}, {self.mode}.)") 


