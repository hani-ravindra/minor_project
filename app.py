# app.py
from flask import Flask, request, jsonify
import joblib
from feature_extractor import extract_features

app = Flask(__name__)
model = joblib.load("phishing_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    features = extract_features(url)
    prediction = model.predict([features])[0]
    label = "Phishing" if prediction == 1 else "Legitimate"

    return jsonify({"url": url, "prediction": label})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
