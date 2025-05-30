from flask import Flask, request, jsonify, render_template
from joblib import load
import numpy as np
from input_process import preprocess

app = Flask(__name__)

model = load('model.joblib')

with open('../Pesian_Stop_Words_List.txt', 'r', encoding='utf-8') as file:
    stop_words = [line.strip() for line in file]

@app.route('/')
def home():
    return render_template('form.html')  

@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.form['text']
        
        processed_text = preprocess(text, stop_words)  
        
        prediction = model.predict_proba(processed_text)
        negative = round(prediction[0][1], 2) * 100
        positive = round(prediction[0][0], 2) * 100
        
        return render_template('form.html', prediction_text=f'\n منفی: {negative}% \n   مثبت: {positive}%')
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
