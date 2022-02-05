# app.py of Seraph #########################################
# Author: @diveyez #########################################
# Flask app configuration and launcher=
#
# connect to db first
import sqlite3

# FLASH APP FOR WEBAPPS
from flask import Flask, render_template # , request, url_for, flash, redirect
# from flask import g
def get_db_connection():
    conn = sqlite3.connect('data/db/database.db')
    conn.row_factory = sqlite3.Row
    return conn
# from flask.sessions import SecureCookieSessionInterface
#from flask_login import * 
#from werkzeug.exceptions import abort

#from seraph_load import *
def seraphAppLauncher():
    return "Seraph is loading..."
def seraphBuild():
    return "Seraph is rebuilding indexes..."# , exec('seraph_main.py')
# do stuff
def seraphWebAppLauncher():
    return "Launching Web App on Localhost"
# do stuff 
app = Flask(__name__)
#app.config['SECRET_KEY'] = 'dsbI1HJft672fd2y8'
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    
    return render_template('index.html', posts=posts), print("WebApp is active...")

# PERMALINKS
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
