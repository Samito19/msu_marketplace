from flask import request
from backend import app
from backend.database import insert_user, validate_credentials
from datetime import datetime
from enum import Enum
import bcrypt
import uuid

class DatabaseErrors(Enum):
    DUPLICATE_USER = 2067

@app.route("/api/v1/")
def server_status():
    return {"server_status": "live", "timestamp": datetime.now()}

@app.route("/api/v1/login", methods=['POST'])
def login():
    email_address = request.form["email_address"]
    password = request.form["password"]
    if validate_credentials(email_address, password):
        return {"status": "SUCCESS"}
    else:
        return {"status": "FAILURE", "details": "AUTH_FAILURE"}

@app.route("/api/v1/register", methods=["POST"])
def register():
    email_address = request.form["email_address"]
    password = request.form["password"]
    hashed_password = bcrypt.hashpw(bytes(password, encoding='utf8'), bcrypt.gensalt())
    new_uuid = str(uuid.uuid4())
    try:
        insert_user(new_uuid, email_address, hashed_password.decode("utf-8"))
        return {"status": "SUCCESS"}
    except Exception as e:
        print(e)
        match e.sqlite_errorcode:
            case DUPLICATE_USER:
                return {"status": "FAILURE", "details": "DUPLICATE_USER"}
