import pandas as pd
import random

# Define value pools
mental_health_options = ['None', 'Mild', 'Severe', 'Undiagnosed', 'In Recovery']
drug_use_options = ['Never', 'Occasional', 'Frequent', 'Addicted', 'Dealer', 'Not Found']
employment_status_options = ['Unemployed', 'Part-Time', 'Full-Time', 'Criminal Income']
crime_type_options = ['Rape', 'Murder', 'Dacoity', 'Theft', 'Fraud', 'Assault', 'Kidnapping', 'Cybercrime', 'Drug Offense', 'Other']

# Score weights (customizable)
mental_score = {'None': 0, 'Mild': 1, 'Severe': 3, 'Undiagnosed': 2, 'In Recovery': 1}
drug_score = {'Never': 0, 'Occasional': 1, 'Frequent': 2, 'Addicted': 4, 'Dealer': 5, 'Not Found': 1}
employment_score = {'Unemployed': 2, 'Part-Time': 1, 'Full-Time': 0, 'Criminal Income': 3}
crime_score = {
    'Rape': 3, 'Murder': 3, 'Dacoity': 2, 'Theft': 1, 'Fraud': 1, 'Assault': 2,
    'Kidnapping': 2, 'Cybercrime': 1, 'Drug Offense': 2, 'Other': 1
}

def generate_entry():
    age = random.randint(8, 80)
    priors = random.randint(0, 100)

    mental = random.choice(mental_health_options)
    drug = random.choice(drug_use_options)
    emp = random.choice(employment_status_options)
    crime = random.choice(crime_type_options)

    # Compute risk score (tweakable)
    score = 0
    score += priors * 0.1  # each prior adds a bit
    score += mental_score[mental]
    score += drug_score[drug]
    score += employment_score[emp]
    score += crime_score[crime]
    score += (age < 18 or age > 65) * 1  # very young or old → slightly higher

    # Threshold: if score ≥ 7.5 → reoffend = 1
    reoffend = 1 if score >= 7.5 else 0

    return [age, priors, mental, drug, emp, crime, reoffend]

# Generate full dataset
rows = [generate_entry() for _ in range(10000)]
df = pd.DataFrame(rows, columns=[
    'Age', 'PriorConvictions', 'MentalHealth', 'DrugUse',
    'EmploymentStatus', 'CrimeType', 'Reoffend'
])

# Save CSV
df.to_csv('../dataset/india_forensic_data.csv', index=False)
print("✅ Dataset saved to dataset/india_forensic_data.csv with 10,000 entries.")
