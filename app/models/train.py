import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
import os
os.makedirs('models', exist_ok=True)

data = pd.read_csv('dataset/bmi.csv')

data['BMI'] = data['Weight'] / ((data['Height']/100) ** 2)

X = data[['BMI']].values
y = data['Index'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f"Training accuracy: {train_score:.2f}")
print(f"Test accuracy: {test_score:.2f}")

with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
category_map = {
    0: "Extremely Underweight",
    1: "Underweight",
    2: "Normal",
    3: "Overweight",
    4: "Obese",
    5: "Extremely Obese"
}


with open('models/category_map.pkl', 'wb') as f:
    pickle.dump(category_map, f)
