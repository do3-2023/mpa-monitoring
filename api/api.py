import os
import json
import psycopg2
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = 0

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")

if not POSTGRES_USER or not POSTGRES_PASSWORD or not POSTGRES_DB or not POSTGRES_HOST:
    raise ValueError("Missing database configuration env variables")

try:
    # Establishing the database connection
    conn = psycopg2.connect(
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=5432
    )

except Exception as err1:
    raise RuntimeError("Cannot connect to the database") from err1

# Open a cursor to perform database operations
cur = conn.cursor()

def init():
    cur.execute("select exists(select * from information_schema.tables where table_name='greetings')")
    if not cur.fetchone()[0]:
        cur.execute("CREATE TABLE greetings (id SERIAL PRIMARY KEY, greeting character varying(255) NOT NULL);")
        cur.execute("INSERT INTO greetings (greeting) VALUES ('Hello world !')")

init()

""" Healthcheck """
@app.route("/healthz")
def health():
    try:
        cur.execute("SELECT * FROM greetings LIMIT(1)")
        return "", 200
    except BaseException as err:
        print(err)
        return "", 500


@app.route("/hello")
def getWord():
    try:
        cur.execute("SELECT greeting FROM greetings LIMIT(1)")
        greetings = cur.fetchone()
    except Exception as err:
        return str(err), 500
    return json.dumps(greetings), 200


@app.route("/persons")
def getAllPersons():
    try:
        cur.execute("SELECT * FROM person")
        persons = cur.fetchall()
    except Exception as err:
        return str(err), 500
    return json.dumps(persons), 200

@app.route("/person", methods = ["POST"])
def insertPerson():
    try:
        person = request.json
        cur.execute(f"INSERT INTO person(last_name, phone_number, location) VALUES {person.get('last_name'), person.get('phone_number'), person.get('location')}")
    except Exception as err:
        return str(err), 500
    return json.dumps("Ok"), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)