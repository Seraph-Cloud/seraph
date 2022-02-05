# Serpah Main Python File #################################
# Author: @diveyez github.com/diveyez diveyez.com #########
# Import Resources ########################################
# Import App sys/env vars #################################
# Import Module and Run From Prompt #######################
###########################################################
# all of this is listed in requirements.txt
# rersources load from module seraph_load.py
# 
from seraph_load import *
# ADD Standalone UI CODE HERE ########################
#
###########################################
print("-----SERAPH------")
print("-------is--------")
print("-----loading-----")
print("--------∆--------")

##############################################################
# MAKE IMAGE DIR's
##############################################################
print("Making data directories if they do not exist...")
if not os.path.exists("data/images"):
    os.mkdir("data/images")
if not os.path.exists("data/images/time_series_plots"):
    os.mkdir("data/images/time_series_plots")
if not os.path.exists("data/images/time_series_plots/1min"):
    os.mkdir("data/images/time_series_plots/1min")
if not os.path.exists("data/images/time_series_plots/5min"):
    os.mkdir("data/images/time_series_plots/5min")
if not os.path.exists("data/images/time_series_plots/15min"):
    os.mkdir("data/images/time_series_plots/15min")
# NEED TO MAKE THE OTHER DIRECTORIES AS WELL ^^^^^^^^^^^^^^^^###
if not os.path.exists("data/csv"):
    os.mkdir("data/csv")
    if not os.path.exists("data/json"):
        os.mkdir("data/json")
# adding the modules path
sys.path.insert(0, 'modules')
sys.path.insert(0, 'seraph_blackhole')
sys.path.insert(0, 'seraph_standalone')
################################################################
# MAKE THINGS HAPPEN BEFORE WEBAPP LAUNCH HERE
# IE: pull data and charts for the webapp on loops set to timers














# EOF ###
#########