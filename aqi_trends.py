
import os
import pickle
import datetime
import pandas as pd
import numpy as np
from prophet import Prophet

# Resolve the path to the Models directory (adjust as needed)
current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, './Models/')

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

# Function to generate dates for past trends starting from yesterday
def generate_past_trend_dates(periods_past):
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    start_date = yesterday - datetime.timedelta(days=periods_past - 1)
    return pd.DataFrame({
        'ds': pd.date_range(start=start_date, end=yesterday)
    })

# Function to reverse log1p transformation if used
def reverse_transform(value):
    return np.expm1(value)

# Function to generate past pollutant trends (including AQI)
def generate_past_pollutant_trends(periods_past):
    trend_dates = generate_past_trend_dates(periods_past)
    city_trends = {}

    for city in os.listdir(model_dir):
        city_path = os.path.join(model_dir, city)
        if os.path.isdir(city_path):  # Check if it's a directory
            city_data = {}

            for model_file in os.listdir(city_path):
                if model_file.endswith('_prophet_model.pkl'):  # Only load Prophet model files
                    region_name = model_file.replace('_prophet_model.pkl', '')
                    model_path = os.path.join(city_path, model_file)

                    try:
                        with open(model_path, 'rb') as file:
                            model = pickle.load(file)

                        # Ensure model compatibility
                        if isinstance(model, dict):  # Multiple pollutants in one model
                            pollutant_data = {}
                            for pollutant, prophet_model in model.items():
                                forecast = prophet_model.predict(trend_dates)

                                # Reverse transformation if log1p was applied during training
                                if 'yhat' in forecast.columns:
                                    forecast['yhat'] = reverse_transform(forecast['yhat'])

                                predictions = forecast['yhat'].apply(int).tolist()

                                pollutant_data[pollutant] = [
                                    {
                                        'date': trend_dates.iloc[i]['ds'].strftime('%Y-%m-%d'),
                                        'value': prediction,
                                        'condition': getCondition(prediction) if pollutant == "AQI" else None,
                                        'class': getConditionClass(prediction) if pollutant == "AQI" else None
                                    }
                                    for i, prediction in enumerate(predictions)
                                ]
                            city_data[region_name] = pollutant_data
                        else:
                            # print(f"Model in {model_file} is not compatible.")
                            pass
                    except Exception as e:
                        # print(f"Error loading or processing model {model_file}: {e}")
                        pass

            city_trends[city] = city_data

    return city_trends

# Main function to get pollutant trends
def get_past_pollutant_trends():
    # Trends for past 30 days
    trends_30_days_past = generate_past_pollutant_trends(periods_past=30)

    # Trends for past 7 days
    trends_7_days_past = generate_past_pollutant_trends(periods_past=7)

    return {
        'trends': {
            '30_days_past': trends_30_days_past,
            '7_days_past': trends_7_days_past
        }
    }

# If running this script directly, invoke the function
if __name__ == "__main__":
    trends = get_past_pollutant_trends()
