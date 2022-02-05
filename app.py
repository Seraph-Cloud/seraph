# app.py of Seraph #########################################
# Author: @diveyez #########################################
# Flask app configuration and launcher
#
#
#from wtforms import StringField, PasswordField, SubmitField
#from flask import FlaskForm as form
#import flask_login
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
from werkzeug.exceptions import abort
from flask.sessions import SecureCookieSessionInterface
from flask import render_template, request, url_for, flash, redirect, g, make_response, abort
import flask as Flask
import requests  # required for interaction and taking data
import os  # required for management of application and files
import time  # required for other modules
import sys  # required for dir creation and file management
import sqlite3  # database for logins and session storagte
import datetime  # time/date
from modules import *
# # will eventually import all
# necessary python scripts as modules from ./modules
from seraph_vars import *  # variable here must be configured
#from seraph_ui import * #imports the vars and ui modules
from seraph_database import *
from json import loads  # required
import json  # required for api's
import pandas as pd  # required
import nasdaqdatalink  # nasda data packages for python
import mplfinance as mf  # finance libraries needed for charting and processing data
import twelvedata  # importing rest of twelvedata
from twelvedata import TDClient  # twelvedata.com's official packages
# CHARTS AND PLOTTING
import plotly  # plotly main package
import plotly.graph_objects as go  # or plotly.express as px
import plotly.io as pio  # import export
import plotly.express as px  # plot charts for usage with twelvedata
# # making sure the parts are loaded, again
# from form import LoginForm  # from login_manager import *
#import importlib
#SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
# EVIL/LIVE
# Necessary Evils Below

# FLASK APP FOR WEBAPPS
app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('data/db/database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


# AUTHENTICATION CODE
# do stuff
app.config['SECRET_KEY'] = 'dsbI1HJft672fd2y8'


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()

    return render_template('index.html', posts=posts)

# PERMALINKS


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
