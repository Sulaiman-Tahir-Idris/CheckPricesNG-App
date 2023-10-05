import pathlib
import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir = basedir)

app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'manufacturers.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#set secret key
app.secret_key = os.urandom(24).hex()


db = SQLAlchemy(app)
ma = Marshmallow(app)