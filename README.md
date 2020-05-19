# Global COVID-19 Analysis

# Summary:
It is March 15th in the United States and we have been watching the world with a growing virus that is spreading all over the world. It is only a matter of time until it begins to hit the United States. There has been quite a bit of talk about the legitimacy of numbers that is being reported.

Here I build a notebook that shows the growing COVID-19 pandemic all around the world and how each country compares to each other. The ability to visualiaze this data will allow us to better understand the seriousness of the issue as well as staying one step ahead of the curve with having up to date knowledge.

# Dataset:
Dataset: Data from https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset - updated daily

Since we are building a framework that with the hopes of continuasly updating the daily feed of released data, we need a data source that is being updated daily, and coming from the Johns Hopkins University Database. The reliability of data will alter per country. This is heavily dependent on the amount of tests that are available, and their daily reporting ability. The W.H.O is working with countries around the world to enhance data collection for continuas and dynamic problem solving and learning about this new virus.

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
    
