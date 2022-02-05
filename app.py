from cProfile import run
# app.py of Seraph
# Author: @diveyez
# Flask app configuration and launcher
import sqlite3 # required
# import subprocess
# for using PHP
from flask import Flask, render_template
# aborts
from werkzeug.exceptions import abort
# connect to db first
# we are using Sqlite and php for web coding with flask
def get_db_connection():
    conn = sqlite3.connect('data/db/database.db')
    conn.row_factory = sqlite3.Row
    return conn
# 404
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post
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
    # FOR USING PHP
    #def phpPages():
    #    out = sp.run(["php", "index.php"], stdout=sp.PIPE)
    #return out.stdout
    return render_template('index.html', posts=posts), print("WebApp is active...")
