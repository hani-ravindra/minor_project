import re
import socket
from urllib.parse import urlparse
import requests

def extract_features(url):
    features = []

    # 1. UsingIP: 1 if IP in URL, else -1
    try:
        socket.inet_aton(urlparse(url).netloc)
        features.append(1)
    except:
        features.append(-1)

    # 2. LongURL: 1 if >= 54 chars, else -1
    features.append(1 if len(url) >= 54 else -1)

    # 3. ShortURL: 1 if using URL shortening service, else -1
    shortening_services = r"bit\.ly|goo\.gl|shorte\.st|tinyurl\.com|t\.co|ow\.ly|bitly\.com|is\.gd|buff\.ly|adf\.ly"
    features.append(1 if re.search(shortening_services, url) else -1)

    # 4. Symbol@ : 1 if '@' in URL, else -1
    features.append(1 if "@" in url else -1)

    # 5. Redirecting // : 1 if more than 1 '//' in URL, else -1
    features.append(1 if url.count("//") > 1 else -1)

    # 6. PrefixSuffix- : 1 if '-' in domain, else -1
    domain = urlparse(url).netloc
    features.append(1 if "-" in domain else -1)

    # 7. SubDomains : 1 if more than 2 dots in domain, else -1
    features.append(1 if domain.count(".") > 2 else -1)

    # 8. HTTPS : 1 if https, else -1
    features.append(1 if urlparse(url).scheme == "https" else -1)

    # 9. DomainRegLen : -1 (placeholder, would need WHOIS)
    features.append(-1)

    # 10. Favicon : -1 (placeholder, would need HTML parsing)
    features.append(-1)

    # 11. NonStdPort : 1 if port not 80/443, else -1
    port = urlparse(url).port
    features.append(-1 if port in [80, 443, None] else 1)

    # 12. HTTPSDomainURL : 1 if 'https' in domain, else -1
    features.append(1 if "https" in domain else -1)

    # 13. RequestURL : -1 (simplified)
    features.append(-1)

    # 14. AnchorURL : -1 (simplified)
    features.append(-1)

    # 15. LinksInScriptTags : -1 (simplified)
    features.append(-1)

    # 16. ServerFormHandler : -1 (simplified)
    features.append(-1)

    # 17. InfoEmail : 1 if '@' in URL, else -1
    features.append(1 if "@" in url else -1)

    # 18. AbnormalURL : 1 if URL contains IP address, else -1
    ip_pattern = r"//\d+\.\d+\.\d+\.\d+"
    features.append(1 if re.search(ip_pattern, url) else -1)

    # 19. WebsiteForwarding : -1 (simplified)
    features.append(-1)

    # 20. StatusBarCust : -1 (simplified)
    features.append(-1)

    # 21. DisableRightClick : -1 (simplified)
    features.append(-1)

    # 22. UsingPopupWindow : -1 (simplified)
    features.append(-1)

    # 23. IframeRedirection : -1 (simplified)
    features.append(-1)

    # 24. AgeofDomain : -1 (placeholder)
    features.append(-1)

    # 25. DNSRecording : -1 (placeholder)
    features.append(-1)

    # 26. WebsiteTraffic : -1 (placeholder)
    features.append(-1)

    # 27. PageRank : -1 (placeholder)
    features.append(-1)

    # 28. GoogleIndex : -1 (placeholder)
    features.append(-1)

    # 29. LinksPointingToPage : -1 (placeholder)
    features.append(-1)

    # 30. StatsReport : -1 (placeholder)
    features.append(-1)

    return features
