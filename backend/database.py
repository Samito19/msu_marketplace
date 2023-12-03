from flask import g
import sqlite3
from enum import Enum
from backend import app, config
import bcrypt

class User(Enum):
    UUID = 0
    EMAIL = 1
    PASSWORD = 2

DATABASE = "msu_marketplace.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def insert_user(uuid, email_address, password):
    db = get_db()
    cur = db.cursor()
    cur.execute(f"INSERT INTO users VALUES (?, ?, ?)", (uuid, email_address, password))
    db.commit()

def validate_credentials(email_address, password):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE email_address = ?", (email_address,))
    user_info = cur.fetchone()
    hashed_pswd = bytes(user_info[2], encoding='utf8')
 
    
    password = bytes(password, encoding='utf8')
    if bcrypt.checkpw(password, hashed_pswd):
        return True
    else:
        return False
