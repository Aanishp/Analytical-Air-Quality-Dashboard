import os
import datetime
import pandas as pd
import pickle
from prophet import Prophet
import numpy as np

# Path to the Models directory
model_dir = "./Models"  # Adjust this path as needed

# Verify if the directory exists
if not os.path.exists(model_dir):
    # print(f"Error: Models directory not found at {os.path.abspath(model_dir)}")
    exit(1)

# Define future dates (next 7 days starting from tomorrow)
future_dates = pd.DataFrame({
    'ds': pd.date_range(start=datetime.datetime.now() + datetime.timedelta(days=1), periods=7)
})

# Functions for AQI conditions, classes, and comments
def getCondition(aqi):
    if aqi <= 50:
        return "Good"
    if aqi <= 100:
        return "Satisfactory"
    if aqi <= 200:
        return "Moderate"
    if aqi <= 300:
        return "Poor"
    if aqi <= 400:
        return "Very Poor"
    return "Severe"

def getConditionClass(aqi):
    if aqi <= 50:
        return "good"
    if aqi <= 100:
        return "satisfactory"
    if aqi <= 200:
        return "moderate"
    if aqi <= 300:
        return "poor"
    if aqi <= 400:
        return "very-poor"
    return "severe"

def getComment(aqi):
    if aqi <= 50:
        return "The air quality is excellent, posing no risk to health."
    if aqi <= 100:
        return "The air quality is acceptable; sensitive individuals may experience minor discomfort."
    if aqi <= 200:
        return "The air quality is tolerable but may cause discomfort to sensitive groups such as children and the elderly."
    if aqi <= 300:
        return "The air quality is unhealthy; prolonged exposure may cause discomfort or health issues."
    if aqi <= 400:
        return "The air quality is very unhealthy; respiratory issues are likely for prolonged exposure."
    return "The air quality is hazardous; even healthy individuals may experience severe health effects."

# Function to load models
def load_model(model_path):
    try:
        with open(model_path, 'rb') as file:
            models = pickle.load(file)
            return models
    except Exception as e:
        # print(f"Error loading model from {model_path}: {e}")
        return None

# Initialize dictionary to store predictions
city_predictions = {}

# Process each city
for city in os.listdir(model_dir):
    city_path = os.path.join(model_dir, city)
    if os.path.isdir(city_path):  # Check if it's a directory
        city_data = {}
        # print(f"Processing models for city: {city}")

        # Process each region
        for model_file in os.listdir(city_path):
            if model_file.endswith('_prophet_model.pkl'):
                region_name = model_file.replace('_prophet_model.pkl', '')  # Extract region name
                model_path = os.path.join(city_path, model_file)

                # Load the model
                models = load_model(model_path)

                if models and "AQI" in models:
                    model = models["AQI"]
                    # print(f"  Loaded AQI model for region: {region_name}")

                    # Predict AQI
                    forecast = model.predict(future_dates)

                    # Inverse log transformation if used
                    forecast['yhat'] = np.expm1(forecast['yhat'])  # Ensure log1p/expm1 consistency

                    # Add predictions to city data
                    aqi_data = [
                        {
                            'date': forecast.iloc[i]['ds'].strftime('%Y-%m-%d'),
                            'AQI': int(forecast.iloc[i]['yhat']),
                            'condition': getCondition(forecast.iloc[i]['yhat']),
                            'class': getConditionClass(forecast.iloc[i]['yhat']),
                            'comment': getComment(forecast.iloc[i]['yhat'])
                        }
                        for i in range(len(forecast))
                    ]
                    city_data[region_name] = aqi_data[-7:]  # Store only the last 7 days
                else:
                    # print(f"  AQI model not found for region: {region_name}")
                    pass

        # Store city's predictions
        city_predictions[city] = city_data


# print(city_predictions)
