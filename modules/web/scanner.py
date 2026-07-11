from core.proxy_handler import get_session
from modules.web.payloads import SSTI_PAYLOADS, SQLI_PAYLOADS
import time

def run_web_probe(args):
    url = args.url
    param = args.param
    proxy = args.proxy
    
    session = get_session(proxy)
    
    print(f"[*] Targeting {url} with param '{param}'")
    
    # Test SSTI
    print("\n[*] Testing for SSTI...")
    for payload in SSTI_PAYLOADS:
        try:
            r = session.get(url, params={param: payload}, timeout=5)
            # If 7*7 evaluates to 49, SSTI is likely present
            if "49" in r.text:
                print(f"[+] SSTI DETECTED! Payload: {payload}")
                return
        except Exception as e:
            print(f"[-] Error with SSTI payload {payload}: {e}")
            time.sleep(1)
    print("[-] No SSTI found.")

    # Test SQLi
    print("\n[*] Testing for SQLi...")
    for payload in SQLI_PAYLOADS:
        try:
            r = session.get(url, params={param: payload}, timeout=5)
            # Basic detection: look for common SQL errors or admin strings
            text_lower = r.text.lower()
            if "sql syntax" in text_lower or "sqlite3.operationalerror" in text_lower or "admin" in text_lower:
                print(f"[+] SQLi DETECTED! Payload: {payload}")
                return
        except Exception as e:
            print(f"[-] Error with SQLi payload {payload}: {e}")
            time.sleep(1)
    print("[-] No SQLi found.")
