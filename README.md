# Project-3---COVID19_vs_H1N1

Tables:
COVID
    - "country_df" = list of all countries in both databases with a unique identifier as Country ID

    - "global_covid_data" = list of all countries effected with total numbers of Confirmed, Deaths, and Recovered
    
    - "global_h1n1_data" = list of all countries effecte with total numbers of Confirmed Cases, Deaths, and end date
    
    - "covid" = Total dataset for covid-19. includes province/state, country, date data was updated, confirmed, deaths, recovered (all cumulative data)
    
    - "h1n1" = Total dataset for H1N1. Includes country, confirmed cases, Deaths, date data was updated (all cumulative data)
    

What graphs do we want to show? 
    - COVID overview by Country
        - Confirmed Cases 
        - Deaths
        - Recovered
        - Mortality Rate
        - Recovered Rate
    - Daily increase in COVID vs daily increase in H1N1 from country selection 
        - Confirmed Cases
        - Deaths
    - Country Comparison with COVID vs H1N1 (all-time data located in global tables)
        - Confirmed Cases
        - Deaths
        - Recovered (for H1N1: Recovered = Cases - Deaths)
    - HeatMap
    
        

How to update database?
    - Enter "python ./run.py" in terminal to execute the script and update the database
