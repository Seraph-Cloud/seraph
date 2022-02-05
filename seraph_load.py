# seraph_load.py of Seraph 
# Author: @diveyez
# Loading essential goodies to the application
# also loading required parts for functionality
import requests # required for interaction and taking data
import os # required for management of application and files
import time # required for other modules
import sys # required for dir creation and file management
import sqlite3 # database for logins and session storagte
import datetime # time/date
##### from modules import * # will eventually import all 
# necessary python scripts as modules from ./modules
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
# FLASH APP FOR WEBAPPS
import flask 
from flask import Flask, render_template, request, url_for, flash, redirect, g
from flask.sessions import SecureCookieSessionInterface
# aborts
from werkzeug.exceptions import abort
# import seraph_login # a modified version of flask_login
from flask_login import * # making sure the parts are loaded, again
#from cProfile import run <- wheere is this from

