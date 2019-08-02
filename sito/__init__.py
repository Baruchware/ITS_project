from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config

app=Flask(__name__)

app.config.from_object(Config)  

db = SQLAlchemy(app)
migrate = Migrate(app, db)
loginmanager = LoginManager(app)


with app.app_context():
	if db.engine.url.drivername == "sqlite":
		migrate.init_app(app, db , render_as_patch=True)
	else:
		migrate.init_app(app,db)   #renderaspatch settato true, qualora il progetto usi sqlite, serve ovviare limitazioni con questo tipo di db, alle modifiche vengono create tabelle "clone"


from sito import models, routes