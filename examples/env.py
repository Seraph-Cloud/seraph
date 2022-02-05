import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path("/env_var/.env"))
print(os.getenv("CONNSTRING"))
# Testing Lines Below Here
#echo(os.getenv())
