# predict.py
import joblib
from feature_extractor import extract_features
# Load trained model
try:
    model = joblib.load("phishing_model.pkl")
    print("Model loaded successfully.\n")
except Exception as e:
    print("Error loading model:", e)
    exit()

while True:
    url = input("Enter a website URL to check (or type 'exit'): ").strip()
    if url.lower() == "exit":
        break

    # Extract features from the URL
    features = extract_features(url)
    
    # Print feature vector for debugging
    print("\nFeature vector used for prediction:")
    feature_names = [
        "UsingIP","LongURL","ShortURL","Symbol@","Redirecting//","PrefixSuffix-",
        "SubDomains","HTTPS","DomainRegLen","Favicon","NonStdPort","HTTPSDomainURL",
        "RequestURL","AnchorURL","LinksInScriptTags","ServerFormHandler","InfoEmail",
        "AbnormalURL","WebsiteForwarding","StatusBarCust","DisableRightClick",
        "UsingPopupWindow","IframeRedirection","AgeofDomain","DNSRecording",
        "WebsiteTraffic","PageRank","GoogleIndex","LinksPointingToPage","StatsReport"
    ]
    for name, value in zip(feature_names, features):
        print(f"{name}: {value}")
    print("Number of features:", len(features))

    # Predict using the trained model
    try:
        prediction = model.predict([features])[0]
        if prediction == 1:
            print(f"\nPhishing Website: {url}\n")
        else:
            print(f"\nLegitimate Website: {url}\n")
    except Exception as e:
        print("Prediction error:", e)
