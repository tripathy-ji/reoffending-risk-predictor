import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv('../dataset/india_forensic_data.csv')

# Encode categorical columns
mental_encoder = LabelEncoder()
df['MentalHealthEncoded'] = mental_encoder.fit_transform(df['MentalHealth'])

drug_encoder = LabelEncoder()
df['DrugUseEncoded'] = drug_encoder.fit_transform(df['DrugUse'])

employment_encoder = LabelEncoder()
df['EmploymentEncoded'] = employment_encoder.fit_transform(df['EmploymentStatus'])

crime_encoder = LabelEncoder()
df['CrimeEncoded'] = crime_encoder.fit_transform(df['CrimeType'])

# Feature matrix
X = df[['Age', 'PriorConvictions', 'MentalHealthEncoded', 'DrugUseEncoded', 'EmploymentEncoded', 'CrimeEncoded']]
y = df['Reoffend']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, 'risk_model.pkl')
joblib.dump(mental_encoder, 'mental_encoder.pkl')
joblib.dump(drug_encoder, 'drug_encoder.pkl')
joblib.dump(employment_encoder, 'employment_encoder.pkl')
joblib.dump(crime_encoder, 'crime_encoder.pkl')

accuracy = model.score(X_test, y_test)
print(f"✅ Saved Random Forest model (accuracy: {accuracy:.2f})")
