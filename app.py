import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort, url_for
from FDataBase import FDataBase

DATABSE = 'bd.db'
DEBUG = True
SECRET_KEY = "dasdsadsa"

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'bd.db')))

menu = [ {"name": "Главная", "url": "/"},
        {"name": " о приложении", "url": "/about"},
        {"name": " обратная связь", "url": "/contact"},
]

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db(): #from app import create_db -> create_db()
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()
    return []

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

dbas = None
@app.before_request
def before_request():
    """установка соединения с БД перед выполнением запроса"""
    global dbase
    db = get_db()
    dbase = FDataBase(db)

@app.route("/")
def index ():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu = dbase.getMenu())

if __name__ == "__main__":
    app.run(debug=True)