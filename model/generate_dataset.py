import pandas as pd
import random

# Set up 500 fake entries
def generate_data(n=500):
    data = []
    for _ in range(n):
        age = random.randint(18, 60)
        prior_convictions = random.randint(0, 10)
        mental_health = random.choice(['None', 'Mild', 'Severe'])
        drug_use = random.choice(['Never', 'Occasional', 'Frequent'])

        # Scoring logic to decide risk
        score = 0
        score += prior_convictions * 2
        score += {'None': 0, 'Mild': 1, 'Severe': 3}[mental_health]
        score += {'Never': 0, 'Occasional': 2, 'Frequent': 4}[drug_use]

        label = 1 if score > 7 else 0  # 1 = Reoffend, 0 = No

        data.append([age, prior_convictions, mental_health, drug_use, label])

    df = pd.DataFrame(data, columns=['Age', 'PriorConvictions', 'MentalHealth', 'DrugUse', 'Reoffend'])
    return df

# Generate and save the dataset
df = generate_data()
df.to_csv('../dataset/forensic_data.csv', index=False)
print("✅ Dataset saved to dataset/forensic_data.csv")
