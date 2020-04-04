# 1. import Flask
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

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
Global_H1N1 = Base.classes.global_h1n1_data

# 2. create an app, being sure to pass name
app = Flask(__name__)

# 3. Define Route
@app.route("/")
def welcome():
    return(
        f"Thank you for using our COVID vs. H1N1 application!</br></br>"

        f"Below are the available routes that can be taken...</br>"
        f"/covid</br>"
        f"/global_covid</br>"
        f"/h1n1</br>"
        f"/global_h1n1</br>"
    )


# @app.route("/covid")
# def covid():

#     # Connect, query, and close session
#     session = Session(engine)
#     results = session.query(
#         Covid.Country, 
#         Covid.Province,
#         Covid.Date,
#         Covid.Confirmed, 
#         Covid.Deaths, 
#         Covid.Recovered
#         ).all()
#     session.close()

#     countries_list = []
#     # val_list = []
    
#     country_dict = {}
#     province_dict = {}
#     data_dict = {}

#     def build_temp_data_dict(date, confirmed, deaths, recovered):
#         temp_data_dict = {
#             "Date": date,
#             "Confirmed": confirmed,
#             "Deaths": deaths,
#             "Recovered": recovered,
#             "Revcovery_Rate": get_rate(recovered, confirmed),
#             "Death_Rate": get_rate(deaths, confirmed)
#         }
#         return(temp_data_dict)


#     for country, province, date, confirmed, deaths, recovered in results:
#         countries_list.append(country)
        
#         if country in country_dict:
#             pass
#         else:
#             country_dict[country] = {}
#             if province is None:
#                 data_dict["Date"].append(date.strftime('%Y-%m-%d'))
#                 data_dict["Confirmed"].append{confirmed}
#                 data_dict["Deaths"].append(deaths)
#                 data_dict["Recovered"].append(recovered)
#                 data_dict["Recovery_Rate"].append(get_rate(recovered, confirmed))
#                 data_dict["Death_Rate"].append(get_rate(deaths, confirmed))
#             else:
            

#         data_dict["Province"] = province
            

#         val_list.append(data_dict)


#     return jsonify(covid_dict)


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

    # def start_country_data_dict(dat, con, dth, rec):
    #     temp_data_dict = {
    #         "Date": [dat],
    #         "Confirmed": [con],
    #         "Deaths": [dth],
    #         "Recovered": [rec],
    #         "Recovery_Rate": [get_rate(rec, con)],
    #         "Death_Rate": [get_rate(dth, con)]
    #     }
    #     return(temp_data_dict)

    def append_country_data_to_dict(cou, dat, con, dth, rec):
        country_dict[cou]["Date"].append(dat)
        country_dict[cou]["Confirmed"].append(con)
        country_dict[cou]["Deaths"].append(dth)
        country_dict[cou]["Recovered"].append(rec)
        country_dict[cou]["Recovery_Rate"].append(get_rate(rec, con))
        country_dict[cou]["Death_Rate"].append(get_rate(dth, con))
    
    for country, date, confirmed, deaths in results:
        recovered = get_recovered(confirmed, deaths)        
        if country in country_dict:
            append_country_data_to_dict(country, date, confirmed, deaths, recovered)
        else:
            country_dict[country] =  {
                "Date": [date],
                "Confirmed": [confirmed],
                "Deaths": [deaths],
                "Recovered": [recovered],
                "Recovery_Rate": [get_rate(recovered, confirmed)],
                "Death_Rate": [get_rate(deaths, confirmed)]
            }
            # {
            #     start_country_data_dict(date, confirmed, deaths, recovered)
            # }

            
            
    return jsonify(country_dict)

# 4. Define main bahavior
if __name__ == "__main__":
    app.run(debug=True)
