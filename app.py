# 1. import Flask
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

import numpy as np 
import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from dateutil.relativedelta import relativedelta
import datetime as dt

engine = create_engine("sqlite:///COVID19_vs_H1N1.sqlite")
conn = engine.connect()

#reflect and exisiting database into a new model
Base = automap_base()

#set up Database
print(engine.table_names())

#reflect the tables
Base.prepare(engine, reflect=True)

#Save reference to the table
Country = Base.classes.country
Covid = Base.classes.covid
H1N1 = Base.classes.h1n1
Global_Covid = Base.classes.global_covid_data
#Global_H1N1 = Base.classes.global_h1n1_data

# 2. create an app, being sure to pass name
app = Flask(__name__)

# 3. Define Route
@app.route("/")
def welcome():
    return(
        f"Thank you for using our COVID vs. H1N1 application!</br>"
        f"Below are the available routes that can be taken...</br>"
        f"/api/v1.0/<state></br>"
    )

@app.route("/country")
def hello():
    session = Session(engine)
    
    results = session.query(Country.Country).all()

    session.close()

    country = []
    for result in results:
        dict = {}
        dict["Country"] = result
        country.append(dict)

    return jsonify(country)


@app.route("/api/v1.0/italy")
def country():
    session = Session(engine)

    results = session.query(Global_Covid.Confirmed, Global_Covid.Deaths, Global_Covid.Recovered).\
        filter(Global_Covid.Country == "Italy").all()

    session.close()

    total_list = []
    for confirmed, deaths, recovered in results:
        dict = {}
        dict["Confirmed"] = confirmed
        dict["Deaths"] = deaths
        dict["Recovered"] = recovered
        dict["Active"] = (confirmed - deaths - recovered)
        total_list.append(dict)

    return jsonify(total_list)


# 4. Define main bahavior
if __name__ == "__main__":
    app.run(debug=True)