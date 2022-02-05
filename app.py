# app.py of Seraph
# Author: @diveyez
# Flask app configuration and launcher
#from cProfile import run <- wheere is this from
import sqlite3 # required
# import subprocess
# for using PHP
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
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
app.config['SECRET_KEY'] = '-dsbI1HJft672.fd2y8'
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

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')