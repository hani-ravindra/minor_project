from flask import Flask, request, jsonify
import joblib
from feature_extractor import extract_features

app = Flask(__name__)
model = joblib.load('phishing_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.get_json()['url']
    features = extract_features(url)
    prediction = model.predict([features])[0]
    result = "Phishing ⚠️" if prediction == 1 else "Legitimate ✅"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
