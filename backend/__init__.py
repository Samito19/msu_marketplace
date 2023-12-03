from configparser import ConfigParser
from flask import Flask, request
from flask_cors import CORS

config = ConfigParser()
config.read("config.ini")

app = Flask(__name__)
cors = CORS(app, resource={
    r"/*":{
        "origins": config["CORSINFO"]["allowed_origin"]
    }
})

from backend import database, auth

