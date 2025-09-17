# features_extractor.py
import re
import requests
import tldextract
from urllib.parse import urlparse

def extract_features(url):
    """
    Extracts 30 features from a URL to match phishing.csv dataset.
    Returns a list of feature values ready for prediction.
    """
    features = []

    # 1. UsingIP: -1 if URL contains IP, 1 otherwise
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    features.append(-1 if re.search(ip_pattern, url) else 1)

    # 2. LongURL: -1 if URL > 75 chars, 0 if 54-75, 1 if <54
    if len(url) < 54:
        features.append(1)
    elif len(url) <= 75:
        features.append(0)
    else:
        features.append(-1)

    # 3. ShortURL: -1 if using tinyurl/bit.ly/etc, 1 otherwise
    shorteners = ['bit.ly','tinyurl','goo.gl','ow.ly','t.co']
    features.append(-1 if any(s in url for s in shorteners) else 1)

    # 4. Symbol@: -1 if '@' in URL
    features.append(-1 if '@' in url else 1)

    # 5. Redirecting//: -1 if '//' appears in path (not after protocol)
    path = urlparse(url).path
    features.append(-1 if '//' in path else 1)

    # 6. PrefixSuffix-: -1 if '-' in domain
    domain = tldextract.extract(url).domain
    features.append(-1 if '-' in domain else 1)

    # 7. SubDomains: -1 if subdomain > 2, 0 if 1-2, 1 if 0
    subdomain_count = len(tldextract.extract(url).subdomain.split('.')) if tldextract.extract(url).subdomain else 0
    if subdomain_count == 0:
        features.append(1)
    elif subdomain_count <= 2:
        features.append(0)
    else:
        features.append(-1)

    # 8. HTTPS: 1 if HTTPS, -1 otherwise
    features.append(1 if urlparse(url).scheme == 'https' else -1)

    # 9. DomainRegLen: placeholder (-1) [needs WHOIS for real]
    features.append(-1)

    # 10. Favicon: placeholder (-1)
    features.append(-1)

    # 11. NonStdPort: -1 if port not 80/443
    parsed = urlparse(url)
    port = parsed.port
    if port is None or port in [80,443]:
        features.append(1)
    else:
        features.append(-1)

    # 12. HTTPSDomainURL: -1 if domain has no HTTPS
    features.append(1 if urlparse(url).scheme == 'https' else -1)

    # 13-15. RequestURL, AnchorURL, LinksInScriptTags: placeholder (-1)
    features.extend([-1, -1, -1])

    # 16-17. ServerFormHandler, InfoEmail: placeholder (-1)
    features.extend([-1, -1])

    # 18. AbnormalURL: placeholder (-1)
    features.append(-1)

    # 19. WebsiteForwarding: placeholder (-1)
    features.append(-1)

    # 20-23. StatusBarCust, DisableRightClick, UsingPopupWindow, IframeRedirection
    features.extend([-1, -1, -1, -1])

    # 24. AgeofDomain: placeholder (-1)
    features.append(-1)

    # 25. DNSRecording: 1 (assuming domain exists)
    features.append(1)

    # 26. WebsiteTraffic: placeholder (-1)
    features.append(-1)

    # 27-30. PageRank, GoogleIndex, LinksPointingToPage, StatsReport: placeholder (-1)
    features.extend([-1, -1, -1, -1])

    return features
