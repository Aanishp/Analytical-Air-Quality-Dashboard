# 🌍 Analytical Air Quality Dashboard  
**Real-time air quality monitoring & forecasting using AQICN API and Prophet model**  

---

## 📌 Project Overview  
The **Analytical Air Quality Dashboard** provides **real-time AQI (Air Quality Index) data**, **7-day air quality predictions**, and **historical trend analysis** for selected cities.  

✅ **Features:**  
- 📡 **Real-time AQI data** from the **AQICN API**  
- 📊 **7-day AQI forecasts** using the **Prophet model**  
- 🌍 **Interactive map visualization** for air quality levels  
- 📈 **Historical trends** (7-day & 30-day) with line & bar graphs  
- 🛠️ **Built with Flask, JavaScript, and Chart.js** for a smooth experience  

---

## 🛠️ Tech Stack  
### 🔹 Backend  
- **Python** (Flask for API handling, Prophet for ML predictions)  
- **Pandas & NumPy** (Data processing & handling missing values)  
- **Requests** (API communication)  

### 🔹 Frontend  
- **HTML, CSS, JavaScript** (User interface)  
- **Chart.js** (Dynamic data visualization)  

---

## 🚀 Installation Guide  

### 🔹 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Aanishp/Analytical-Air-Quality-Dashboard.git
cd Analytical-Air-Quality-Dashboard
```

### 🔹 2️⃣ Install Required Packages
```bash
pip install flask pandas numpy requests prophet
```

### 🔹 3️⃣ Set Up API Key  

To access real-time AQI data, you need an **API key** from **[AQICN API](https://aqicn.org/data-platform/token/)**.  

#### **📌 Step 1: Get Your API Key**  
1. Go to **[AQICN API](https://aqicn.org/data-platform/token/)** and sign up for an API key.  
2. Copy the API key after registration.  

#### **📌 Step 2: Add API Key in Specific Locations**  
You need to place the API key in **two files**:  

##### **1️⃣ In `real_time_fetcher.py` (Line 4)**  
Modify **line 4** of `real_time_fetcher.py` to add the API key:  

```python
API = "YOUR_API_KEY_HERE"
```
##### **2️⃣ In `./templates/index.html` (Lines 112, 128, and 173)**
Replace `your_api_key_here` in the following lines:

🔹 `Line 112:`

```javascript
var WAQI_URL =
        "https://tiles.waqi.info/tiles/usepa-aqi/{z}/{x}/{y}.png?token=YOUR_API_KEY_HERE";
```

🔹 `Line 128:`

```javascript
var url = `https://api.waqi.info/feed/geo:${userLat};${userLng}/?token=YOUR_API_KEY_HERE`;
```

🔹 `Line 173:`
```javascript
var url = `https://api.waqi.info/feed/geo:${e.latlng.lat};${e.latlng.lng}/?token=YOUR_API_KEY_HERE`;
```

#### 🔹 4️⃣ Run the Flask Server
```bash
python main.py
```
The server should start at `http://127.0.0.1:5000/`

---

## 📊 Project Workflow
- 1️⃣ User selects a city/region
- 2️⃣ Flask backend fetches real-time AQI via AQICN API
- 3️⃣ Prophet model predicts AQI for the next 7 days
- 4️⃣ Data is processed & visualized using Chart.js
- 5️⃣ User views live AQI, predictions & historical trends

---
## 📸 Screenshots

### Home Page 
![Home Page](https://i.imgur.com/AhAodsf.png)  

### City Selection Menu on AQI Dashboard
![City Selection Menu on AQI Dashboard](https://i.imgur.com/b69gLNS.png)

### Location Selection Menu on AQI Dashboard
![Location Selection Menu on AQI Dashboard](https://i.imgur.com/YPmWdNI.png)

### Air Quality Dashboard 
![Air Quality Dashboard](https://i.imgur.com/lmnSkwA.png)

### Historical AQI Trends Over 30 Days - Bar Graph
![Historical AQI Trends Over 30 Days - Bar Graph](https://i.imgur.com/PIQDWJV.png)

### Historical AQI Trends Over 30 Days - Line Graph
![Historical AQI Trends Over 30 Days - Line Graph](https://i.imgur.com/GXj0tm8.png)

---

## Dataset  
The dataset for this project was collected from the [IUDX Catalogue](https://catalogue.cos.iudx.org.in/).

---
## 📽️ Video Demo  

▶️ **[Click here to watch the demo](https://drive.google.com/file/d/1P2UsH3STNUt8N0VhEt5EW4uWc3LDXADD/view?usp=drive_link)**  

🔹 This video demonstrates the **Analytical Air Quality Dashboard** in action, showcasing real-time AQI monitoring, forecasts, and historical trends.
  
---

## 👥 Team Members  
🚀 [Aanish P](https://github.com/Aanishp)  
🚀 [MS Prajwal](https://github.com/prajwal504)  
🚀 [B. Vamshi Nandhan Reddy](https://github.com/VamshiNandhanReddy)  
🚀 [Anushka Srivastava](https://github.com/anushka073)  

📍 **Department of Artificial Intelligence & Machine Learning**  
📍 **BMS Institute of Technology & Management, Bengaluru** 

---
