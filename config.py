import os

basedir = os.path.abspath(os.path.dirname(__file__)) #in questa variabile ce la locazione del progetto

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'blog.db') #crea db nella directory pre segnata
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # previene l invio di segnali in fase di modifica per velocizzare l app
