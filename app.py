from cProfile import run
# app.py of Seraph
# Author: @diveyez
# Flask app configuration and launcher
import sqlite3 # required
from flask import Flask, render_template
# connect to db first
# we are using Sqlite and php for web coding with flask
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
from seraph_main import *
def seraphAppLauncher():
    return "Seraph is loading..."
def seraphBuild():
    return "Seraph is rebuilding indexes...", exec('seraph_main.py')
def seraphWebAppLauncher():
    return "Launching Web App on Localhost" # do stuff 
app = Flask(__name__)
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts), print("WebApp is active...")
