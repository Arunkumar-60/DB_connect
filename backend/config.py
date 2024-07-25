# imports
from flask import flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# CORS = cross origin request

# inisializing the flask app 
app = Flask(__name__)
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///db_connect.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

db = SQLAlchemy(app)
