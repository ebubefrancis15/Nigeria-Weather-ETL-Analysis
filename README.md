# Nigeria Weather ETL Pipeline & Analysis

## Project Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline for collecting and analysing weather data across Nigeria's 36 states and the Federal Capital Territory (FCT).

Weather data was collected using the OpenWeather API, processed and transformed using Python and Pandas, and saved as a structured CSV dataset for further analysis.

The project also examines weather patterns across Nigeria's six geopolitical zones.

---

## Project Objective

The objectives of this project are to:

- Extract weather data from the OpenWeather API.
- Collect weather information for Nigeria's 36 states and the FCT.
- Transform and clean the collected data using Python and Pandas.
- Map each state to its geopolitical zone.
- Analyse temperature, humidity, pressure and wind speed across the zones.
- Identify differences in weather conditions between geopolitical zones.
- Create meaningful insights from the processed dataset.
- Demonstrate an end-to-end ETL workflow.

---

## Data Source

Weather data was obtained using the OpenWeather API.

The API provides current weather information for specified locations.

**Data source:** OpenWeather API

---

## Technologies Used

- Python
- Pandas
- Requests
- Jupyter Notebook
- OpenWeather API
- Matplotlib
- GitHub

---

## ETL Pipeline

The project follows three major stages:

### 1. Extract

Weather data was extracted from the OpenWeather API for Nigeria's 36 states and the Federal Capital Territory.

The extracted information includes:

- State
- Geopolitical Zone
- Temperature
- Feels Like Temperature
- Humidity
- Atmospheric Pressure
- Wind Speed
- Weather Condition

### 2. Transform

The extracted data was processed using Python and Pandas.

Transformation activities included:

- Creating a structured dataset.
- Mapping states to geopolitical zones.
- Cleaning and formatting the data.
- Checking for missing values.
- Checking the dataset structure and data types.
- Performing descriptive statistical analysis.
- Sorting and grouping data for analysis.

### 3. Load

The transformed dataset was saved as:

`weather_data.csv`

The dataset contains weather information for 37 locations representing Nigeria's 36 states and the FCT.

---

## Dataset Description

The final dataset contains the following variables:

| Column | Description |
|---|---|
| State | Nigerian state or FCT |
| Geopolitical_Zone | Geopolitical zone of the state |
| Temperature_C | Temperature in degrees Celsius |
| Feels_Like_C | Feels-like temperature in degrees Celsius |
| Humidity_% | Relative humidity percentage |
| Pressure_hPa | Atmospheric pressure in hectopascals |
| Wind_Speed_mps | Wind speed in metres per second |
| Weather | General weather condition |

---

## Data Validation

The processed dataset was checked for:

- Missing values
- Data types
- Dataset structure
- Duplicate records
- Correct geopolitical zone assignments

The final dataset contained 37 records representing Nigeria's 36 states and the FCT.

---

## Business Questions

The analysis was designed around the following questions:

1. Which geopolitical zone has the highest average temperature?
2. Which geopolitical zone has the highest average humidity?
3. Which Nigerian states currently have the highest and lowest temperatures?
4. Which states have the highest wind speeds?
5. Which geopolitical zones show the greatest temperature variation?
6. What differences in weather conditions can be observed across Nigeria's geopolitical zones?

---

## Key Findings

### Temperature

The North Central zone recorded the highest average temperature at approximately **29.67°C**.

The South West zone recorded the lowest average temperature at approximately **23.95°C** among the six geopolitical zones.

### Humidity

The South West recorded the highest average humidity at approximately **96.33%**.

The North East recorded the lowest average humidity at approximately **58.00%**.

### State Temperature Differences

The hottest state in the analysed dataset was **Borno**, with a temperature of approximately **31.09°C**.

The coolest state was **Osun**, with a temperature of approximately **21.85°C**.

### Wind Speed

The analysis showed variation in wind speeds across states, with **Yobe** recording the highest observed wind speed at approximately **4.82 m/s** among the results analysed.

### Temperature Variation

The **North Central** zone showed the greatest temperature variation, with a temperature range of approximately **4.96°C**.

---

## Business Insights

The analysis demonstrates that weather conditions differ considerably across Nigeria's geopolitical zones.

The Northern zones generally showed higher temperatures and lower humidity compared with some Southern zones.

The South West recorded particularly high humidity, while the North East showed considerably lower humidity.

The variation in temperature and wind conditions across states demonstrates the importance of considering geographical location when analysing weather patterns in Nigeria.

---

## Recommendations

Based on the analysis:

1. **Consider geographical differences when making weather-related decisions.**  
   Weather conditions vary considerably between Nigeria's geopolitical zones, so national-level decisions should account for regional differences.

2. **Use weather data to support operational planning.**  
   Businesses involved in agriculture, transportation, logistics and outdoor activities can incorporate weather information into their planning processes.

3. **Monitor temperature and humidity patterns.**  
   Areas experiencing higher temperatures or humidity may require additional planning for activities sensitive to weather conditions.

4. **Continue collecting historical weather data.**  
   The current dataset represents weather conditions at the time of extraction. Maintaining historical records would allow more detailed trend and seasonal analysis.

5. **Automate the ETL process.**  
   The pipeline can be scheduled to collect updated weather information regularly, creating a continuously refreshed dataset for monitoring.

---

## Visualizations

The project includes visualizations showing:

- Weather conditions across Nigerian states.
- Temperature comparisons.
- Temperature and moving/derived weather measures where applicable.
- Geopolitical zone comparisons.
- Weather variability across zones.

These visualizations help communicate the differences observed in the dataset.

---

## Project Files

| File | Description |
|---|---|
| `Nigeria_Weather_ETL_Analysis.ipynb` | Jupyter Notebook containing the complete ETL process and analysis |
| `weather_etl.py` | Python script containing the ETL pipeline |
| `weather_data.csv` | Processed weather dataset |

---

## Skills Demonstrated

This project demonstrates practical experience in:

- Python programming
- Pandas
- API data extraction
- Data cleaning
- Data transformation
- ETL pipeline development
- Data validation
- Data analysis
- Data visualization
- Working with geographical datasets
- GitHub project management

---

## Conclusion

This project demonstrates an end-to-end ETL workflow using real-time weather data from the OpenWeather API.

Weather information was extracted for Nigeria's 36 states and the FCT, transformed into a structured dataset, mapped to geopolitical zones and analysed to identify regional differences.

The analysis revealed notable differences in temperature, humidity, wind speed and temperature variation across Nigeria's geopolitical zones.

The project provides a foundation that can be extended with automated data collection, historical weather tracking and more advanced time-series analysis.

---

## Author

**Francis Okafor**

Data Analytics Project – Week 7

#Python #DataAnalytics #ETL #Pandas #DataScience #APIs #Nigeria #AnalystLabAfrica
