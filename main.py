# Import Libraries
import pickle
from flask import Flask, request, jsonify

# Load trained model
with open("fake_news_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

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

        # Directly make prediction with the raw text
        prediction = model.predict([text])[0]  # Assuming model works with raw text

        # Return JSON response
        result = {"prediction": "REAL" if prediction == 1 else "FAKE"}
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
