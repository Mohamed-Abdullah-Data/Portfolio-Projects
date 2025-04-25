import pandas as pd

import openpyxl

# READ IN THE CSV FILE AS A PANDAS DATAFRAME
bikes = pd.read_csv('C:\\Users\\cakef\\Documents\\Dropbox\\London Bike Sharing Dataset\\london_merged.csv')

# EXPLORE THE DATA
print(bikes.info())

# FIRST 5 ROWS
print(bikes.head())

# COUNT THE UNIQUE VALUES IN THE WEATHER_CODE COLUMN
print(bikes.weather_code.value_counts())

# COUNT THE UNIQUE VALUES IN THE SEASON COLUMN
print(bikes.season.value_counts())

# SPECIFYING THE COLUMN NAMES THAT I WANT TO USE
new_cols_dict ={
    'timestamp':'TIME',
    'cnt':'COUNT',
    't1':'TEMP_REAL_C',
    't2':'TEMP_FEELS_LIKE_C',
    'hum':'HUMIDITY_PERCENT',
    'wind_speed':'WIND_SPEED_KPH',
    'weather_code':'WEATHER',
    'is_holiday':'IS_HOLIDAY',
    'is_weekend':'IS_WEEKEND',
    'season':'SEASON'
}

# RENAMING THE COLUMNS TO THE SPECIFIED COLUMN NAMES
bikes.rename(new_cols_dict, axis=1, inplace=True)

# CHANGING THE HUMIDITY VALUES TO PERCENTAGE (I.E. A VALUE BETWEEN 0 AND 1)
bikes.HUMIDITY_PERCENT = bikes.HUMIDITY_PERCENT / 100

# CREATING A SEASON DICTIONARY SO THAT WE CAN MAP THE INTEGERS 0-3 TO THE ACTUAL WRITTEN VALUES
season_dict = {
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'autumn',
    '3.0':'winter'
}

# CREATING A WEATHER DICTIONARY SO THAT WE CAN MAP THE INTEGERS TO THE ACTUAL WRITTEN VALUES
weather_dict = {
    '1.0':'Clear',
    '2.0':'Scattered clouds',
    '3.0':'Broken clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'Snowfall'
}

# CHANGING THE SEASON COLUMN DATA TYPE TO STRING
bikes.SEASON = bikes.SEASON.astype('str')
# MAPPING THE VALUES 0-3 TO THE ACTUAL WRITTEN SEASONS
bikes.SEASON = bikes.SEASON.map(season_dict)

# CHANGING THE WEATHER COLUMN DATA TYPE TO STRING
bikes.WEATHER = bikes.WEATHER.astype('str')
# MAPPING THE VALUES TO THE ACTUAL WRITTEN WEATHERS
bikes.WEATHER = bikes.WEATHER.map(weather_dict)

# CHECKING OUR DATAFRAME TO SEE IF THE MAPPINGS HAVE WORKED
print(bikes.head())

# WRITING THE FINAL DATAFRAME TO AN EXCEL FILE THAT I WILL USE IN MY TABLEAU VISUALISATION
bikes.to_excel('C:\\Users\\cakef\\Desktop\\processed_data.xlsx', index=False)




