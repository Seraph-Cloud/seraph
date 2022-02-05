# app.py of Seraph #########################################
# Author: @diveyez #########################################
# Flask app configuration and launcher
# connect to db first
import sqlite3
def get_db_connection():
    conn = sqlite3.connect('data/db/database.db')
    conn.row_factory = sqlite3.Row
    return conn
# FLASH APP FOR WEBAPPS
from flask import Flask, render_template, request, url_for, flash, redirect, g
from flask.sessions import SecureCookieSessionInterface
from flask_login import * 
# Loading essential goodies to the application
# also loading required parts for functionality
import requests # required for interaction and taking data
import os # required for management of application and files
import time # required for other modules
import sys # required for dir creation and file management
import datetime # time/date
from seraph_vars import * # variable here must be configured
from seraph_ui import * #imports the vars and ui modules
from seraph_database import *
from json import loads # required
import json # required for api's
import pandas as pd # required
import nasdaqdatalink # nasda data packages for python
import mplfinance as mf # finance libraries needed for charting and processing data
import twelvedata # importing rest of twelvedata 
from twelvedata import TDClient #twelvedata.com's official packages
# CHARTS AND PLOTTING
import plotly # plotly main package
import plotly.graph_objects as go  # or plotly.express as px
import plotly.io as pio # import export
import plotly.express as px # plot charts for usage with twelvedata
# aborts
from werkzeug.exceptions import abort
# import seraph_login # a modified version of flask_login
# making sure the parts are loaded, again
#from cProfile import run
#from login_manager import *
#from mixins import *
#from utils import *
#from signals import *
import importlib

#from seraph_load import *
def seraphAppLauncher():
    return print("Seraph is loading...")
def seraphBuild():
    return print("Seraph is rebuilding indexes...") # , exec('seraph_main.py')
# do stuff
def seraphWebAppLauncher():
    return print("Launching Web App on Localhost") 
# do stuff 
app = Flask(__name__)
app.config['SECRET_KEY'] = '-dsbI1HJft672.fd2y8'
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
