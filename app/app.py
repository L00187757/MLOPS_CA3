from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model and category mapping
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
with open('models/category_map.pkl', 'rb') as f:
    category_map = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        height = float(data['height']) / 100  # Convert cm to meters
        weight = float(data['weight'])
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        
        # Predict category
        prediction = model.predict([[bmi]])[0]
        category = category_map.get(prediction, "Unknown")
        
        return jsonify({
            'bmi': round(bmi, 2),
            'category': category,
            'prediction_code': int(prediction)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
