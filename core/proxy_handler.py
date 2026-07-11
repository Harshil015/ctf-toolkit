import requests
import urllib3

# Disable SSL warnings for local CTF environments and self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_session(proxy=None):
    """
    Returns a requests.Session object.
    If a proxy is provided, it configures the session to route through it 
    and disables SSL verification (useful for Burp Suite).
    """
    session = requests.Session()
    
    if proxy:
        session.proxies = {"http": proxy, "https": proxy}
        session.verify = False  # Trust Burp's CA or ignore SSL errors
        print(f"[*] Proxy enabled: {proxy}")
        
    return session
