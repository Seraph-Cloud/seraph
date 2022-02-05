# seraph_load.py of Seraph 
# Author: @diveyez
# Loading essential goodies to the application
from modules import * # will eventually import all 
# necessary python scripts as modules from ./modules
from seraph_vars import * # imports the vars module
import plotly.graph_objects as go  # or plotly.express as px
import nasdaqdatalink # nasda data packages for python
import mplfinance as mf # finance libraries needed for charting and processing data
import pandas as pd # required
from twelvedata import TDClient #twelvedata.com's official packages
import plotly.express as px # plot charts for usage with twelvedata
import plotly # plotly main package
import plotly.io as pio # import export
import twelvedata # importing rest of twelvedata 
# ^ not necessary after development and testing
from json import loads # required
import json # required for api's
import requests # required for interaction and taking data
import os # required for management of application and files
import time # required for other modules
import sys # required for dir creation and file management