from backend import app, database
from datetime import datetime

@app.route("/api/v1/")
def server_status():
    cur = database.get_db().cursor()
    cur.execute("CREATE TABLE movie(title, year, score)")
    return {"server_status": "live", "timestamp": datetime.now()}

@app.route("/api/v1/login", methods=['POST'])
def login():
    email_address = request.form["email_address"]
    password = request.form["password"]
    print(f"Received {email_address} and {password}")
    return {"status": "SUCCESS"}

