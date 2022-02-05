# app.py of Seraph
# Author: @diveyez
# Flask app configuration and launcher
# Broken, Rebuilding
#
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
