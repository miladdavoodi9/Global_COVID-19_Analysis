# Global COVID-19 Analysis
Dataset: Data from https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset - updated daily

Part 1: Notebook Analysis (COVID_19_analysis_global.ipynb)
- Jupyter Notebook shows global analysis for COVID-19
  - Country comparison for cases, deaths, and recovered
  - Mortality Rate
  - Recover Rate
  - Italy day-by-day
  - USA day-by-day
  - Global Visualizations
  - GeoMap timelapse

Part 2: Visualization and H1N1 Comparison
ETL Program:
 - Download new Dataset and load into "Resources"
 - Enter "python ./run.py" in terminal to execute the script and update the SQLite database
    - This will create all the necessary tables (shown below), create sqlite database with correct schema.
 - Run app.py (Flask app)

Tables:
COVID
    - "country_df" = list of all countries in both databases with a unique identifier as Country ID

    - "global_covid_data" = list of all countries effected with total numbers of Confirmed, Deaths, and Recovered
    
    - "global_h1n1_data" = list of all countries effecte with total numbers of Confirmed Cases, Deaths, and end date
    
    - "covid" = Total dataset for covid-19. includes province/state, country, date data was updated, confirmed, deaths, recovered (all cumulative data)
    
    - "h1n1" = Total dataset for H1N1. Includes country, confirmed cases, Deaths, date data was updated (all cumulative data)
    
