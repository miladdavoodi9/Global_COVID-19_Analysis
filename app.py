# 1. import Flask
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import pandas as pd
import numpy as np 
import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from dateutil.relativedelta import relativedelta
import datetime as dt

# Auxiliary functions
def get_recovered(con, ded):
    try:
        return(con - ded)
    except TypeError:
        return(0)

def get_rate(input_value, conf):
    try:
        return(input_value / conf)
    except (ZeroDivisionError, TypeError):
        return(0)
    
def append_data_to_dict(input_dict, cou, dat, con, dth, rec):
    input_dict[cou]["Date"].append(dat)
    input_dict[cou]["Confirmed"].append(con)
    input_dict[cou]["Deaths"].append(dth)
    input_dict[cou]["Recovered"].append(rec)
    input_dict[cou]["Recovery_Rate"].append(get_rate(rec, con))
    input_dict[cou]["Death_Rate"].append(get_rate(dth, con))

def start_data_dict(input_dict, cou, dat, con, dth, rec):
    input_dict[cou] = {
        "Date": [dat],
        "Confirmed": [con],
        "Deaths": [dth],
        "Recovered": [rec],
        "Recovery_Rate": [get_rate(rec, con)],
        "Death_Rate": [get_rate(dth, con)]
    }




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
Covid_2 = Base.classes.covid
H1N1 = Base.classes.h1n1
Global_Covid = Base.classes.global_covid_data
Global_H1N1 = Base.classes.global_h1n1_data

# 2. create an app, being sure to pass name
app = Flask(__name__)

# 3. Define Route
@app.route("/")
def home():
    return render_template("global_h1n1.html")
#    return(
#         f"Thank you for using our COVID vs. H1N1 application!</br></br>"
#         f"Below are the available routes that can be taken...</br>"
#         f"/covid</br>"
#         f"/global_covid</br>"
#         f"/h1n1</br>"
#         f"/global_h1n1</br>")

@app.route("/C")
def covid_page():
    return render_template("covid.html")
@app.route("/Top_Countries")
def selected_countries():
    return render_template("Top_Countries_COVID.html")

@app.route("/covid")
def covid():

    # Connect, query, and close session
    session = Session(engine)
    results = session.query(
        Covid_2.Country, 
        Covid_2.Date,
        Covid_2.Confirmed, 
        Covid_2.Deaths, 
        Covid_2.Recovered
        ).all()
    session.close()

    country_dict = {}
 
    for country, date, confirmed, deaths, recovered in results:
        if country in country_dict.keys():
            append_data_to_dict(country_dict, country, date, confirmed, deaths, recovered)
        else:
            start_data_dict(country_dict, country, date, confirmed, deaths, recovered)

    return jsonify(country_dict)

@app.route("/global_covid")
def global_covid():

    # Connect, query, and close session
    session = Session(engine)
    results = session.query(
        Global_Covid.Country, 
        Global_Covid.Confirmed, 
        Global_Covid.Deaths, 
        Global_Covid.Recovered
        ).all()
    session.close()


    key_list = []
    val_list = []

    for country, confirmed, deaths, recovered in results:
        key_list.append(country)
        
        temp_dict = {}
        temp_dict["Confirmed"] = confirmed
        temp_dict["Deaths"] = deaths
        temp_dict["Recovered"] = recovered
        temp_dict["Recovery_Rate"] = get_rate(recovered, confirmed)
        temp_dict["Death_Rate"] = get_rate(deaths, confirmed)
        val_list.append(temp_dict)

    global_covid_dict = dict(zip(key_list, val_list))

    return jsonify(global_covid_dict)


@app.route("/global_h1n1")
def global_h1n1():

    # Connect, query, and close session
    session = Session(engine)
    results = session.query(
        Global_H1N1.Country, 
        Global_H1N1.Confirmed, 
        Global_H1N1.Deaths, 
        ).all()
    session.close()

    key_list = []
    val_list = []

    for country, confirmed, deaths in results:
        key_list.append(country)
        
        temp_dict = {}
        temp_dict["Confirmed"] = confirmed
        temp_dict["Deaths"] = deaths
        temp_recovered = get_recovered(confirmed, deaths)
        temp_dict["Recovered"] = temp_recovered
        temp_dict["Recovery_Rate"] = get_rate(temp_recovered, confirmed)
        temp_dict["Death_Rate"] = get_rate(deaths, confirmed)
        val_list.append(temp_dict)

    global_h1n1_dict = dict(zip(key_list, val_list))

    return jsonify(global_h1n1_dict)

@app.route("/h1n1")
def h1n1():

    # Connect, query, and close session
    session = Session(engine)
    results = session.query(
        H1N1.Country, 
        H1N1.Date,
        H1N1.Confirmed, 
        H1N1.Deaths, 
        ).all()
    session.close()

    country_dict = {}
 
    for country, date, confirmed, deaths in results:
        recovered = get_recovered(confirmed, deaths)        
        if country in country_dict.keys():
            append_data_to_dict(country_dict, country, date, confirmed, deaths, recovered)
        else:
            start_data_dict(country_dict, country, date, confirmed, deaths, recovered)
            
            
    return jsonify(country_dict)

@app.route("/global_h1n1_graph_data")
def global_h1n1_graph(): 
    session = Session(engine)
    results = session.query(
        Global_H1N1.Country, 
        Global_H1N1.Confirmed, 
        Global_H1N1.Deaths, 
        ).all()
    session.close()
    
    countries = []
    confirmed_cases = []
    death_count = []
    for (country, confirmed, deaths) in results: 
        countries.append(country)
        confirmed_cases.append(confirmed)
        death_count.append(deaths)
    
    # Generate the plot trace
    # trace1 = {
    #     "x": countries,
    #     "y": confirmed_cases,
    #     type:'bar'
    # }
    # trace2 = {
    #     "x": countries,
    #     "y": death_count, 
    #     type: 'bar'
    # }
    # data = [trace1, trace2]
    # graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    # # return render_template('global_h1n1.html', graphJSON=graphJSON)
    return jsonify(countries, confirmed_cases, death_count)
# 4. Define main bahavior
if __name__ == "__main__":
    app.run(debug=True)
