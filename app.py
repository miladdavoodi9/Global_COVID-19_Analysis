# 1. import Flask
from flask import Flask, jsonify
import numpy as np 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from dateutil.relativedelta import relativedelta
import datetime as dt 

#set up Database
engine = create_engine("sqlite:///...")

#reflect and exisiting database into a new model
Base = automap_base()
#reflect the tables
Base.prepare(engine,reflect=True)

#Save reference to the table
table1 = Base.classes.table_name
table2 = Base.classes.table_name 

# 2. create an app, being sure to pass name
app = Flask(__name__)

# 4. Define main bahavior
if __name__ == "__main__":
    app.run(debug=True)