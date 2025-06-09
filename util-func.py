# %% [code] {"jupyter":{"outputs_hidden":false}}
import datetime
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

def get_CO_subindex(x):
    if pd.isna(x):  # Check if the value is NaN
        return 0
    if x <= 4.4:
        result = x * 50 / 4.4
    elif x <= 9.4:
        result = 50 + (x - 4.4) * (100 - 50) / (9.4 - 4.4)
    elif x <= 12.4:
        result = 100 + (x - 9.4) * (150 - 100) / (12.4 - 9.4)
    elif x <= 15.4:
        result = 150 + (x - 12.4) * (200 - 150) / (15.4 - 12.4)
    elif x <= 30.4:
        result = 200 + (x - 15.4) * (300 - 200) / (30.4 - 15.4)
    elif x <= 50.4:
        result = 300 + (x - 30.4) * (500 - 300) / (50.4 - 30.4)
    else:
        result = 500 + (x - 50.4) * (999 - 500) / (99999.9 - 50.4)
    
    return round(result, 2)

# Function to calculate NO2 Sub-Index
def get_NO2_subindex(x):
    if pd.isna(x):  # Check if the value is NaN
        return 0
    if x <= 53:
        return x * 50 / 53
    elif x <= 100:
        return 50 + (x - 54) * (100 - 50) / (100 - 54)
    elif x <= 360:
        return 100 + (x - 101) * (150 - 100) / (360 - 101)
    elif x <= 649:
        return 150 + (x - 361) * (200 - 150) / (649 - 361)
    elif x <= 1249:
        return 200 + (x - 650) * (300 - 200) / (1249 - 650)
    elif x <= 2049:
        return 300 + (x - 1250) * (500 - 300) / (2049 - 1250)
    else:
        return 500 + (x - 2049) * (999 - 500) / (99999 - 2049)

    return round(result, 2)  

def get_O3_subindex(x):
    if pd.isna(x):  # Check if the value is NaN
        return 0
    if x <= 0.054:
        return x * 50 / 0.054
    elif x <= 0.070:
        return 50 + (x - 0.054) * (100 - 50) / (0.070 - 0.054)
    elif x <= 0.085:
        return 100 + (x - 0.070) * (150 - 100) / (0.085 - 0.070)
    elif x <= 0.105:
        return 150 + (x - 0.085) * (200 - 150) / (0.105 - 0.085)
    elif x <= 0.200:
        return 200 + (x - 0.105) * (300 - 200) / (0.200 - 0.105)
    else:
        return 300 + (x - 0.200) * (500 - 300) / (99999 - 0.200)
        
    return round(result, 2) 

def get_PM10_subindex(x):
    if pd.isna(x):  # Check if the value is NaN
        return 0
    if x <= 54.0:
        return x * 50 / 54.0
    elif x <= 154.0:
        return 50 + (x - 54.0) * (100 - 50) / (154.0 - 54.0)
    elif x <= 254.0:
        return 100 + (x - 154.0) * (150 - 100) / (254.0 - 154.0)
    elif x <= 354.0:
        return 150 + (x - 254.0) * (200 - 150) / (354.0 - 254.0)
    elif x <= 424.0:
        return 200 + (x - 354.0) * (300 - 200) / (424.0 - 354.0)
    elif x <= 604.0:
        return 300 + (x - 424.0) * (500 - 300) / (604.0 - 424.0)
    else:
        return 500  # If the value is above 604.0 µg/m³, the AQI is capped at 500

    return round(result, 2) 

def get_PM25_subindex(x):
    if pd.isna(x):  # Check if the value is NaN
        return 0
    if x <= 12.0:
        return x * 50 / 12.0
    elif x <= 35.4:
        return 50 + (x - 12.1) * (100 - 50) / (35.4 - 12.1)
    elif x <= 55.4:
        return 100 + (x - 35.5) * (150 - 100) / (55.4 - 35.5)
    elif x <= 150.4:
        return 150 + (x - 55.5) * (200 - 150) / (150.4 - 55.5)
    elif x <= 250.4:
        return 200 + (x - 150.5) * (300 - 200) / (250.4 - 150.5)
    elif x <= 350.4:
        return 300 + (x - 250.5) * (400 - 300) / (350.4 - 250.5)
    elif x <= 500.4:
        return 400 + (x - 350.5) * (500 - 400) / (500.4 - 350.5)
    else:
        return 500  # If the value is above 500.4 µg/m³, the AQI is capped at 500

    return round(result, 2) 

def get_SO2_subindex(x):
    if pd.isna(x):  # Check if the value is NaN
        return 0
    if x <= 35.0:
        return x * 50 / 35.0
    elif x <= 75.0:
        return 50 + (x - 36.0) * (100 - 50) / (75.0 - 36.0)
    elif x <= 185.0:
        return 100 + (x - 76.0) * (150 - 100) / (185.0 - 76.0)
    elif x <= 304.0:
        return 150 + (x - 186.0) * (200 - 150) / (304.0 - 186.0)
    elif x <= 604.0:
        return 200 + (x - 305.0) * (300 - 200) / (604.0 - 305.0)
    elif x <= 804.0:
        return 300 + (x - 605.0) * (400 - 300) / (804.0 - 605.0)
    elif x <= 1004.0:
        return 400 + (x - 805.0) * (500 - 400) / (1004.0 - 805.0)
    else:  # For values greater than 1004 µg/m³
        return 500

    return round(result, 2) 

# More Info: https://www.epa.gov/system/files/documents/2024-02/pm-naaqs-air-quality-index-fact-sheet.pdf

def calculate_aqi(data, subindex_columns=['PM2.5_Subindex', 'PM10_Subindex', 'SO2_Subindex', 'NO2_Subindex', 'CO_Subindex', 'O3_Subindex']):
    # Count non-zero sub-indices for each row
    data["Checks"] = data[subindex_columns].gt(0).sum(axis=1)

    # Calculate AQI as the maximum of all sub-indices
    data["AQI"] = data[subindex_columns].max(axis=1)

    # Constraints:
    # 1: Both PM2.5 and PM10 sub-indices are zero, AQI is set to 0
    data.loc[
        (data["pm25"] == 0) & 
        (data["pm10"] == 0), 
        "AQI"
    ] = 0

    # 2: If less than 3 pollutants have non-zero sub-indices, AQI is set to 0
    data.loc[data["Checks"] < 3, "AQI"] = 0

    # Round AQI to the nearest integer
    data["AQI"] = data["AQI"].round()

    return data

def get_AQI_bucket(x):
    if x <= 50:
        return "Good"
    elif x <= 100:
        return "Moderate"
    elif x <= 150:
        return "Unhealthy for Sensitive Groups"
    elif x <= 200:
        return "Unhealthy"
    elif x <= 300:
        return "Very Unhealthy"
    elif x > 300:
        return "Hazardous"
    else:
        return np.NaN