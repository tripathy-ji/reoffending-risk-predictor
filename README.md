# 🔍 Reoffending Risk Predictor

A machine learning-powered web app to predict the risk of reoffending (recidivism) based on synthetic forensic patterns inspired by Indian NCRB data.

Built with:
- 🧠 Machine Learning (Random Forest)
- 🐍 Python & Flask
- 📊 Synthetic data from NCRB-style insights
- 🌐 Hosted on Render

## 🔗 Live Demo

👉 [Visit the App](https://reoffending-risk-app.onrender.com/)  
_(May take a few seconds to load on free hosting)_

---

## 📌 Features

- Simple input form for Age, Prior Convictions, Mental Health, Drug Use, Employment, Crime Type
- Risk predicted using a trained ML model
- Categorical encodings saved & reused via `joblib`
- Clean web UI using HTML and Bootstrap
- Trained on realistic Indian-style synthetic data (~10,000 rows)

---

## 📁 Project Structure

```bash
├── app.py                   # Flask app
├── templates/
│   └── index.html           # HTML frontend
├── model/
│   ├── risk_model.pkl       # Trained model
│   ├── *_encoder.pkl        # Label encoders
│   └── train_model.py       # ML training script
├── dataset/
│   └── india_forensic_data.csv  # Synthetic dataset
├── generate_indian_data.py # Dataset generator
└── requirements.txt         # Dependencies
