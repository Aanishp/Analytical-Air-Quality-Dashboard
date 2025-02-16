import requests

# API Configuration
API = "YOUR_API_KEY_HERE"
links = {
    'delhi': {
        "alipur": "https://api.waqi.info/feed/@11266/",
        "pusa": "https://api.waqi.info/feed/@10124/",
        "r.k.-puram": "https://api.waqi.info/feed/@2556/"
    },
    'bangalore': {
        'hebbal': "https://api.waqi.info/feed/@11428/",
        'btm-layout': "https://api.waqi.info/feed/@8190/",
        'peenya': "https://api.waqi.info/feed/@3758/"
    },
    'hyderabad': {
        'icrisat-patancheru': "https://api.waqi.info/feed/@11305/",
        "ida-pashamylaram": "https://api.waqi.info/feed/@9144/",
        "zoo-park": "https://api.waqi.info/feed/@8677/"
    },
    'thiruvananthapuram': {
        "kariavattom": "https://api.waqi.info/feed/@12824/",
        "plammoodu": "https://api.waqi.info/feed/@9585/"
    }
}
param = {"token": API}

# Helper functions
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

def get_aqi_status(aqi):
    if aqi <= 50:
        return ('Good', ['#00e400', '#00e400'])
    elif 51 <= aqi <= 100:
        return ('Moderate', ['#ffcc00', '#ff8800'])
    elif 101 <= aqi <= 150:
        return ('Unhealthy for Sensitive Groups', ['#ff8800', '#ff4400'])
    elif 151 <= aqi <= 200:
        return ('Unhealthy', ['#ff4400', '#cc0000'])
    elif 201 <= aqi <= 300:
        return ('Very Unhealthy', ['#99004c', '#66001b'])
    else:
        return ('Hazardous', ['#7e0023', '#7e0023'])

# Fetch data for all locations
def fetch_aqi_data():
    all_data = {}

    for city, regions in links.items():
        city_data = {}
        for region, url in regions.items():
            response = requests.get(url, params=param)
            data = response.json()

            if data.get('status') == 'ok':
                aqi = data['data']['aqi']
                pm10 = data['data']['iaqi'].get('pm10', {}).get('v', None)
                pm25 = data['data']['iaqi'].get('pm25', {}).get('v', None)
                timestamp = data['data']['time']['s']

                status, gradient = get_aqi_status(aqi)
                condition = getCondition(aqi)
                condition_class = getConditionClass(aqi)
                comment = getComment(aqi)

                city_data[region] = {
                    'aqi': aqi,
                    'pm10': pm10,
                    'pm25': pm25,
                    'timestamp': timestamp,
                    'status': status,
                    'gradient': gradient,
                    'condition': condition,
                    'class': condition_class,
                    'comment': comment
                }
            else:
                city_data[region] = {
                    'error': "Failed to fetch data. Check the API or network."
                }

        all_data[city] = city_data

    return all_data

# Expose the real-time data
real_time_data = fetch_aqi_data()
