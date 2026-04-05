Ambient Weather Station Dashboard

A full-stack web app built around an Ambient Weather station. It pulls real-time sensor data, stores it in MongoDB, and gives you a proper dashboard to look at current readings, historical trends, and ML-based forecasts.


What it does

- Pulls live data from the weather station every hour, with a DB fallback if the API is slow
- Shows historical charts for temperature, humidity, wind, pressure, and rainfall at different resolutions (5-min, hourly, daily)
- Runs a Keras neural net to generate 10-day forecasts
- Separately predicts daily rainfall using an XGBoost regressor (log1p-transformed to handle the heavy-zero imbalance in rain data)
- Tracks forecast accuracy over time with MAE and RMSE against actual observed readings
- Has a chatbot that can answer weather questions and let you download historical data as CSV
- Basic login/signup for access control


Stack

- Frontend – React, TailwindCSS, Recharts
- Backend – Node.js + Express, Mongoose
- ML – Python, TensorFlow/Keras, XGBoost, scikit-learn, pandas
- AI – Groq SDK, Google Generative AI
- DB – MongoDB


Folder structure

```
miniproject/
├── frontend/             # React app
├── server.js             # Express entry point
├── routes/               # weather + auth routes
├── models/               # Mongoose schemas
├── ml/
│   ├── train_model.py        # Keras model training
│   ├── train_rain_model.py   # XGBoost rain model training
│   ├── predict.py            # 10-day forecast generation
│   ├── predict_rain.py       # Rainfall forecast
│   └── backtest_rain.py      # Accuracy backtesting
└── utils/                # Ambient Weather API wrapper, DB sync
```


Setup

Requirements: Node.js, Python 3.8+, MongoDB

1. Install backend deps:
   ```bash
   npm install
   ```

2. Install frontend deps:
   ```bash
   cd frontend && npm install
   ```

3. Create a `.env` in the root:
   ```env
   PORT=3000
   MONGODB_URI=your_mongodb_uri
   AMBIENT_WEATHER_API_KEY=your_api_key
   AMBIENT_WEATHER_APP_KEY=your_app_key
   GROQ_API_KEY=your_groq_key
   ```

4. Install Python deps:
   ```bash
   cd ml && pip install -r requirements.txt
   ```


Running it

Backend:
```bash
npm start
```

Frontend (separate terminal):
```bash
cd frontend && npm start
```


API routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/api/weather` | Latest readings (cached, DB fallback) |
| GET | `/api/weather/history` | Historical data (`days`, `resolution` params) |
| GET | `/api/weather/forecast` | 10-day ML forecast (1hr cache) |
| GET | `/api/weather/accuracy` | Forecast accuracy vs actuals |
| GET | `/api/weather/rain-accuracy` | Rainfall backtest results |
| GET | `/api/weather/export` | Download as CSV |
| POST | `/api/auth/login` | Login |
| POST | `/api/auth/signup` | Signup |
