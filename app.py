from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load model and encoders
model = joblib.load('model/risk_model.pkl')
mental_encoder = joblib.load('model/mental_encoder.pkl')
drug_encoder = joblib.load('model/drug_encoder.pkl')
employment_encoder = joblib.load('model/employment_encoder.pkl')
crime_encoder = joblib.load('model/crime_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        age = int(data['age'])
        prior_convictions = int(data['prior_convictions'])
        mental = data['mental_health'].strip().title()
        drug = data['drug_use'].strip().title()
        employment = data['employment_status'].strip().title()
        crime = data['crime_type'].strip().title()

        mental_encoded = mental_encoder.transform([mental])[0]
        drug_encoded = drug_encoder.transform([drug])[0]
        employment_encoded = employment_encoder.transform([employment])[0]
        crime_encoded = crime_encoder.transform([crime])[0]

        features = [[age, prior_convictions, mental_encoded, drug_encoded, employment_encoded, crime_encoded]]
        prediction = model.predict(features)[0]

        result = "High Risk" if prediction == 1 else "Low Risk"
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

