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

🚀 How to Run Locally

git clone https://github.com/tripathy-ji/reoffending-risk-predictor.git
cd reoffending-risk-predictor
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py

Then open http://127.0.0.1:5000

🧠 Tech Stack
Python

Flask

scikit-learn

HTML + Bootstrap

Joblib

👤 Author
Ayush Tripathy
B.Sc Forensic Science, NFSU Dharwad
LinkedIn Profile : https://www.linkedin.com/in/ayush-tripathy-5666a631a

🌐 Live Demo
👉 Hosted on Render : https://reoffending-risk-app.onrender.com

📄 License
MIT License. Use freely with attribution.

---

#### 📌 Step 3: Click **"Commit Changes"** at the bottom of the page.

✅ Done! Your GitHub `README.md` will now have a polished layout, full instructions, your screenshot, live link, and tech stack.

---

#### ❗ Reminder: Make sure your image file is actually uploaded and accessible

Your image (e.g., `screenshot.png`) must be:

- Uploaded to your repo
- In the main root folder (or update the path accordingly in the Markdown)
- You can rename your screenshot to `screenshot.png` to match the path above.

Let me know when you've done this, and I’ll take a final look to confirm everything’s perfect for sharing 💪


