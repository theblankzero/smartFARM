# 🌱 Fertilizer Recommendation System (ANN + IoT + Supabase)

This project predicts the best fertilizer based on **real-time soil data** (NPK, pH, Humidity, Temperature).

- **ANN Model** trained on Kaggle dataset  
- **Flask Web App** for predictions & UI  
- **Supabase** for storing IoT data  
- **ESP32 IoT Device** to send sensor readings  

## 🚀 Setup
```bash
git clone https://github.com/YOUR_USERNAME/fertilizer-recommendation-ann-iot.git
cd fertilizer-recommendation-ann-iot
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
python finalferti.py    # Train ANN model (saves to /models)
python main.py          # Run web app
```

## 🌍 Access
- Web: http://127.0.0.1:5000/iot  
- API: http://127.0.0.1:5000/api/iot  

## 🔧 IoT ESP32 Setup
Upload `esp32/esp32_supabase.ino` to ESP32 (Arduino IDE).  
Update WiFi & Supabase credentials inside the file.  
