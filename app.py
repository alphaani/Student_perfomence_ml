from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# LOAD THE FILE HERE
model = joblib.load('student_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Extract values from React request
    # Make sure these match the names in your React form
    hours = float(data['hours'])
    attendance = float(data['attendance'])
    participation = float(data['participation'])
    
    # Format data for the model [[hour, attend, part]]
    input_data = np.array([[hours, attendance, participation]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    return jsonify({'score': float(prediction[0])})

if __name__ == '__main__':
    app.run(port=5000)