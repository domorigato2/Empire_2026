import urllib.request
import json
import sys

def fetch_api_data(url):
    print("\n==================================================")
    print("      REST API SCOUT // JSON TELEMETRY PARSER     ")
    print("==================================================")
    print(f" Target Endpoint : {url}")
    print(" Executing GET request...")
    print("--------------------------------------------------")

    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'EmpireAPI-Scout/1.0'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            status_code = response.getcode()
            body = response.read().decode('utf-8')
            data = json.loads(body)
            
            print(f" HTTP Status Code : {status_code} [OK]")
            print(f" Data Type        : {type(data).__name__}")
            print("--------------------------------------------------")
            print(" Parsed JSON Payload Preview:")
            
            if isinstance(data, dict):
                for k, v in list(data.items())[:6]:
                    print(f"    --> {k}: {str(v)[:60]}")
            elif isinstance(data, list):
                print(f"    --> List contains {len(data)} items. First item:")
                print(f"    --> {str(data[0])[:100]}")
            else:
                print(f"    --> {str(data)[:100]}...")
                
    except Exception as e:
        print(f"[!] API Extraction Failed: {e}")

    print("==================================================\n")

if __name__ == "__main__":
    target_url = sys.argv[1] if len(sys.argv) > 1 else "https://api.github.com/repos/domorigato2/Empire_2026"
    fetch_api_data(target_url)
