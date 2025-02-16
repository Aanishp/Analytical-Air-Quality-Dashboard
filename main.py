from flask import Flask, render_template
from sevendaypred import city_predictions
from aqi_trends import get_past_pollutant_trends
from real_time_fetcher import real_time_data
from cal import get_data

# Call the function
trends = get_past_pollutant_trends()


local_server = True
app = Flask(__name__)
app.secret_key='12345678'

# Main page
@app.route('/')
def home_page():
    return render_template('index.html')

# Delhi
@app.route('/delhi')
def delhi_page():
    return render_template('delhi.html')

@app.route('/alipur')
def alipur_page():
    trend_30 = trends['trends']['30_days_past']['Delhi']["alipur,-delhi-air-quality"]
    trend_7 = trends['trends']['7_days_past']['Delhi']["alipur,-delhi-air-quality"]
    real_time = real_time_data["delhi"]['alipur']
    predict_7 = city_predictions['Delhi']['alipur,-delhi-air-quality']
    aqi_trend_7 = get_data(trend_7, "AQI")
    aqi_trend_30 = get_data(trend_30, "AQI")
    pm25_trend_30 = get_data(trend_30, "pm25")
    pm10_trend_30 = get_data(trend_30, "pm10")
    co_trend_30 = get_data(trend_30, "co")
    so2_trend_30 = get_data(trend_30, "so2")
    no2_trend_30 = get_data(trend_30, "no2")
    o3_trend_30 = get_data(trend_30, "o3")

    return render_template('alipur.html',real_time = real_time, predict_7 = predict_7, aqi_trend_7 = aqi_trend_7, aqi_trend_30 = aqi_trend_30, pm25_trend_30 = pm25_trend_30, pm10_trend_30 = pm10_trend_30, co_trend_30 = co_trend_30, so2_trend_30 = so2_trend_30, no2_trend_30 = no2_trend_30, o3_trend_30 = o3_trend_30)

@app.route('/pusa')
def pusa_page():
    trend_30 = trends['trends']['30_days_past']['Delhi']["pusa,-delhi-air-quality"]
    trend_7 = trends['trends']['7_days_past']['Delhi']["pusa,-delhi-air-quality"]
    real_time = real_time_data["delhi"]['pusa']
    predict_7 = city_predictions['Delhi']['pusa,-delhi-air-quality']
    aqi_trend_7 = get_data(trend_7, "AQI")
    aqi_trend_30 = get_data(trend_30, "AQI")
    pm25_trend_30 = get_data(trend_30, "pm25")
    pm10_trend_30 = get_data(trend_30, "pm10")
    co_trend_30 = get_data(trend_30, "co")
    so2_trend_30 = get_data(trend_30, "so2")
    no2_trend_30 = get_data(trend_30, "no2")
    o3_trend_30 = get_data(trend_30, "o3")

    return render_template('pusa.html',real_time = real_time, predict_7 = predict_7, aqi_trend_7 = aqi_trend_7, aqi_trend_30 = aqi_trend_30, pm25_trend_30 = pm25_trend_30, pm10_trend_30 = pm10_trend_30, co_trend_30 = co_trend_30, so2_trend_30 = so2_trend_30, no2_trend_30 = no2_trend_30, o3_trend_30 = o3_trend_30)

@app.route('/rkpuram')
def rkpuram_page():
    trend_30 = trends['trends']['30_days_past']['Delhi']["r.k.-puram, delhi-air-quality"]
    trend_7 = trends['trends']['7_days_past']['Delhi']["r.k.-puram, delhi-air-quality"]
    real_time = real_time_data["delhi"]['r.k.-puram']
    predict_7 = city_predictions['Delhi']['r.k.-puram, delhi-air-quality']
    aqi_trend_7 = get_data(trend_7, "AQI")
    aqi_trend_30 = get_data(trend_30, "AQI")
    pm25_trend_30 = get_data(trend_30, "pm25")
    pm10_trend_30 = get_data(trend_30, "pm10")
    co_trend_30 = get_data(trend_30, "co")
    so2_trend_30 = get_data(trend_30, "so2")
    no2_trend_30 = get_data(trend_30, "no2")
    o3_trend_30 = get_data(trend_30, "o3")
    return render_template('rkpuram.html', real_time = real_time, predict_7 = predict_7, aqi_trend_7 = aqi_trend_7, aqi_trend_30 = aqi_trend_30, pm25_trend_30 = pm25_trend_30, pm10_trend_30 = pm10_trend_30, co_trend_30 = co_trend_30, so2_trend_30 = so2_trend_30, no2_trend_30 = no2_trend_30, o3_trend_30 = o3_trend_30)

# Bangalore
@app.route('/bangalore')
def bangalore_page():
    return render_template('bangalore.html')

@app.route('/btm-layout')
def btm_layout_page():
    trend_30 = trends['trends']['30_days_past']['Bangalore']["btm,-bangalore-air-quality"]
    trend_7 = trends['trends']['7_days_past']['Bangalore']["btm,-bangalore-air-quality"]
    real_time = real_time_data["bangalore"]['btm-layout']
    predict_7 = city_predictions['Bangalore']['btm,-bangalore-air-quality']
    aqi_trend_7 = get_data(trend_7, "AQI")
    aqi_trend_30 = get_data(trend_30, "AQI")
    pm25_trend_30 = get_data(trend_30, "pm25")
    pm10_trend_30 = get_data(trend_30, "pm10")
    co_trend_30 = get_data(trend_30, "co")
    so2_trend_30 = get_data(trend_30, "so2")
    no2_trend_30 = get_data(trend_30, "no2")
    o3_trend_30 = get_data(trend_30, "o3")
    return render_template('btm-layout.html', real_time = real_time, predict_7 = predict_7, aqi_trend_7 = aqi_trend_7, aqi_trend_30 = aqi_trend_30, pm25_trend_30 = pm25_trend_30, pm10_trend_30 = pm10_trend_30, co_trend_30 = co_trend_30, so2_trend_30 = so2_trend_30, no2_trend_30 = no2_trend_30, o3_trend_30 = o3_trend_30)

@app.route('/hebbal')
def hebbal_page():
    trend_30 = trends['trends']['30_days_past']['Bangalore']["hebbal,-bengaluru-air-quality"]
    trend_7 = trends['trends']['7_days_past']['Bangalore']["hebbal,-bengaluru-air-quality"]
    real_time = real_time_data["bangalore"]['hebbal']
    predict_7 = city_predictions['Bangalore']['hebbal,-bengaluru-air-quality']
    aqi_trend_7 = get_data(trend_7, "AQI")
    aqi_trend_30 = get_data(trend_30, "AQI")
    pm25_trend_30 = get_data(trend_30, "pm25")
    pm10_trend_30 = get_data(trend_30, "pm10")
    co_trend_30 = get_data(trend_30, "co")
    so2_trend_30 = get_data(trend_30, "so2")
    no2_trend_30 = get_data(trend_30, "no2")
    o3_trend_30 = get_data(trend_30, "o3")

    return render_template('hebbal.html',real_time = real_time, predict_7 = predict_7, aqi_trend_7 = aqi_trend_7, aqi_trend_30 = aqi_trend_30, pm25_trend_30 = pm25_trend_30, pm10_trend_30 = pm10_trend_30, co_trend_30 = co_trend_30, so2_trend_30 = so2_trend_30, no2_trend_30 = no2_trend_30, o3_trend_30 = o3_trend_30)

@app.route('/peenya')
def peenya_page():
    trend_30 = trends['trends']['30_days_past']['Bangalore']["peenya,-bangalore-air-quality"]
    trend_7 = trends['trends']['7_days_past']['Bangalore']["peenya,-bangalore-air-quality"]
    real_time = real_time_data["bangalore"]['peenya']
    predict_7 = city_predictions['Bangalore']['peenya,-bangalore-air-quality']
    aqi_trend_7 = get_data(trend_7, "AQI")
    aqi_trend_30 = get_data(trend_30, "AQI")
    pm25_trend_30 = get_data(trend_30, "pm25")
    pm10_trend_30 = get_data(trend_30, "pm10")
    co_trend_30 = get_data(trend_30, "co")
    so2_trend_30 = get_data(trend_30, "so2")
    no2_trend_30 = get_data(trend_30, "no2")
    o3_trend_30 = get_data(trend_30, "o3")
    return render_template('peenya.html',real_time = real_time, predict_7 = predict_7, aqi_trend_7 = aqi_trend_7, aqi_trend_30 = aqi_trend_30, pm25_trend_30 = pm25_trend_30, pm10_trend_30 = pm10_trend_30, co_trend_30 = co_trend_30, so2_trend_30 = so2_trend_30, no2_trend_30 = no2_trend_30, o3_trend_30 = o3_trend_30)

# hyderabad
@app.route('/hyderabad')
def hyderabad_page():
    return render_template('hyderabad.html')

@app.route('/icrisat-patancheru')
def icrisat_patancheru_page():
    trend_30 = trends['trends']['30_days_past']['Hyderabad']["icrisat-patancheru, hyderabad-air-quality"]
    trend_7 = trends['trends']['7_days_past']['Hyderabad']["icrisat-patancheru, hyderabad-air-quality"]
    real_time = real_time_data["hyderabad"]['icrisat-patancheru']
    predict_7 = city_predictions['Hyderabad']['icrisat-patancheru, hyderabad-air-quality']
    aqi_trend_7 = get_data(trend_7, "AQI")
    aqi_trend_30 = get_data(trend_30, "AQI")
    pm25_trend_30 = get_data(trend_30, "pm25")
    pm10_trend_30 = get_data(trend_30, "pm10")
    co_trend_30 = get_data(trend_30, "co")
    so2_trend_30 = get_data(trend_30, "so2")
    no2_trend_30 = get_data(trend_30, "no2")
    o3_trend_30 = get_data(trend_30, "o3")
    return render_template('icrisat-patancheru.html', real_time = real_time, predict_7 = predict_7, aqi_trend_7 = aqi_trend_7, aqi_trend_30 = aqi_trend_30, pm25_trend_30 = pm25_trend_30, pm10_trend_30 = pm10_trend_30, co_trend_30 = co_trend_30, so2_trend_30 = so2_trend_30, no2_trend_30 = no2_trend_30, o3_trend_30 = o3_trend_30)

@app.route('/ida-pashamylaram')
def ida_pashamylaram_page():
    trend_30 = trends['trends']['30_days_past']['Hyderabad']["ida-pashamylaram, hyderabad-air-quality"]
    trend_7 = trends['trends']['7_days_past']['Hyderabad']["ida-pashamylaram, hyderabad-air-quality"]
    real_time = real_time_data["hyderabad"]['ida-pashamylaram']
    predict_7 = city_predictions['Hyderabad']['ida-pashamylaram, hyderabad-air-quality']
    aqi_trend_7 = get_data(trend_7, "AQI")
    aqi_trend_30 = get_data(trend_30, "AQI")
    pm25_trend_30 = get_data(trend_30, "pm25")
    pm10_trend_30 = get_data(trend_30, "pm10")
    co_trend_30 = get_data(trend_30, "co")
    so2_trend_30 = get_data(trend_30, "so2")
    no2_trend_30 = get_data(trend_30, "no2")
    o3_trend_30 = get_data(trend_30, "o3")
    return render_template('ida-pashamylaram.html', real_time = real_time, predict_7 = predict_7, aqi_trend_7 = aqi_trend_7, aqi_trend_30 = aqi_trend_30, pm25_trend_30 = pm25_trend_30, pm10_trend_30 = pm10_trend_30, co_trend_30 = co_trend_30, so2_trend_30 = so2_trend_30, no2_trend_30 = no2_trend_30, o3_trend_30 = o3_trend_30)

@app.route('/zoopark-bahadurpurawest')
def zoopark_bahadurpurawest_page():
    trend_30 = trends['trends']['30_days_past']['Hyderabad']["zoo-park, bahadurpura west, hyderabad-air-quality"]
    trend_7 = trends['trends']['7_days_past']['Hyderabad']["zoo-park, bahadurpura west, hyderabad-air-quality"]
    real_time = real_time_data["hyderabad"]['zoo-park']
    predict_7 = city_predictions['Hyderabad']['zoo-park, bahadurpura west, hyderabad-air-quality']
    aqi_trend_7 = get_data(trend_7, "AQI")
    aqi_trend_30 = get_data(trend_30, "AQI")
    pm25_trend_30 = get_data(trend_30, "pm25")
    pm10_trend_30 = get_data(trend_30, "pm10")
    co_trend_30 = get_data(trend_30, "co")
    so2_trend_30 = get_data(trend_30, "so2")
    no2_trend_30 = get_data(trend_30, "no2")
    o3_trend_30 = get_data(trend_30, "o3")
    return render_template('zoopark-bahadurpurawest.html', real_time = real_time, predict_7 = predict_7, aqi_trend_7 = aqi_trend_7, aqi_trend_30 = aqi_trend_30, pm25_trend_30 = pm25_trend_30, pm10_trend_30 = pm10_trend_30, co_trend_30 = co_trend_30, so2_trend_30 = so2_trend_30, no2_trend_30 = no2_trend_30, o3_trend_30 = o3_trend_30)

# Thiruvananthapuram
@app.route('/thiruvananthapuram')
def thiruvananthapuram_page():
    return render_template('thiruvananthapuram.html')

@app.route('/kariavattom')
def kariavattom_page():
    trend_30 = trends['trends']['30_days_past']['Thiruvananthapuram']["kariavattom,-thiruvananthapuram-air-quality"]
    trend_7 = trends['trends']['7_days_past']['Thiruvananthapuram']["kariavattom,-thiruvananthapuram-air-quality"]
    real_time = real_time_data["thiruvananthapuram"]['kariavattom']
    predict_7 = city_predictions['Thiruvananthapuram']['kariavattom,-thiruvananthapuram-air-quality']
    aqi_trend_7 = get_data(trend_7, "AQI")
    aqi_trend_30 = get_data(trend_30, "AQI")
    pm25_trend_30 = get_data(trend_30, "pm25")
    pm10_trend_30 = get_data(trend_30, "pm10")
    co_trend_30 = get_data(trend_30, "co")
    so2_trend_30 = get_data(trend_30, "so2")
    no2_trend_30 = get_data(trend_30, "no2")
    o3_trend_30 = get_data(trend_30, "o3")
    return render_template('kariavattom.html', real_time = real_time, predict_7 = predict_7, aqi_trend_7 = aqi_trend_7, aqi_trend_30 = aqi_trend_30, pm25_trend_30 = pm25_trend_30, pm10_trend_30 = pm10_trend_30, co_trend_30 = co_trend_30, so2_trend_30 = so2_trend_30, no2_trend_30 = no2_trend_30, o3_trend_30 = o3_trend_30)

@app.route('/plammoodu')
def plammoodu_page():
    trend_30 = trends['trends']['30_days_past']['Thiruvananthapuram']["plammoodu,-thiruvananthapuram-air-quality"]
    trend_7 = trends['trends']['7_days_past']['Thiruvananthapuram']["plammoodu,-thiruvananthapuram-air-quality"]
    real_time = real_time_data["thiruvananthapuram"]['plammoodu']
    predict_7 = city_predictions['Thiruvananthapuram']['plammoodu,-thiruvananthapuram-air-quality']
    aqi_trend_7 = get_data(trend_7, "AQI")
    aqi_trend_30 = get_data(trend_30, "AQI")
    pm25_trend_30 = get_data(trend_30, "pm25")
    pm10_trend_30 = get_data(trend_30, "pm10")
    co_trend_30 = get_data(trend_30, "co")
    so2_trend_30 = get_data(trend_30, "so2")
    no2_trend_30 = get_data(trend_30, "no2")
    o3_trend_30 = get_data(trend_30, "o3")
    return render_template('plammoodu.html', real_time = real_time, predict_7 = predict_7, aqi_trend_7 = aqi_trend_7, aqi_trend_30 = aqi_trend_30, pm25_trend_30 = pm25_trend_30, pm10_trend_30 = pm10_trend_30, co_trend_30 = co_trend_30, so2_trend_30 = so2_trend_30, no2_trend_30 = no2_trend_30, o3_trend_30 = o3_trend_30)

app.run(debug=True)