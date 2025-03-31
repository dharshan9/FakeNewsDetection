

# Import Libraries
import pickle
import numpy as np
from flask import Flask, request, jsonify

# Load trained model and vectorizer
with open("fake_news_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

# Initialize Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return "Fake News Detection API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input text
        data = request.json
        text = data.get("text", "")

        # Convert text to TF-IDF vector
        text_vector = vectorizer.transform([text]).toarray()

        # Make prediction
        prediction = model.predict(text_vector)[0]

        # Return JSON response
        result = {"prediction": "REAL" if prediction == 1 else "FAKE"}
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
