from cProfile import run
from flask import Flask, render_template
from seraph_main import *
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
def seraphAppLauncher():
    return "Seraph is loading..."
def seraphBuild():
    return "Seraph is rebuilding indexes...", exec('seraph_main.py')
def seraphWebAppLauncher():
    return "Launching Web App on Localhost" # do stuff 