from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)


db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models, commands

