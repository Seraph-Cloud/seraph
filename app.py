# app.py of Seraph
# Author: @diveyez
# Flask app configuration and launcher
#from cProfile import run <- wheere is this from
import sqlite3 # required
# import subprocess
# for using PHP
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, login
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

# PERMALINKS
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
# CREATE NEW POST
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
# EDIT POST
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))
# AUTHENTICATION CODE
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"
login_manager.login_message = u"You must be logged in to view this page."
login_manager.login_message_category = "info"
login_manager.anonymous_user = guest
login_manager.refresh_view = "accounts.reauthenticate"
login_manager.needs_refresh_message = (
    u"To protect your account, please reauthenticate to access this page."
)
login_manager.needs_refresh_message_category = "info"
@login_manager.user_loader
# FUNCTIONS
def load_user(user_id):
    return User.get(user_id)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)
@app.route("/settings")
@login_required
def settings():
    pass
@app.route("/logout")

@login_required
def logout():
    logout_user()
    return redirect(somewhere)
@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return ()
@login_manager.request_loader
def load_user_from_request(request):

    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(alternative_id=user_id).first()
def get_id(self):
    return unicode(self.alternative_id)