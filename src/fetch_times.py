import os

import requests
from dotenv import load_dotenv

# 1. Load the .env file so os.getenv can see your key
load_dotenv()
api_key = os.getenv("PRAYER_API_KEY")
if not api_key:
    raise SystemExit("PRAYER_API_KEY is missing - check your .env file")

# 2. Where the API lives
url = "https://www.londonprayertimes.com/api/times/"

# 3. The parameters the API expects (a dictionary of name: value)
params = {
    "format": "json",                  
    "key": api_key,                     
    "24hours": "true",                 
}

# 4. Ask the API for today's times
response = requests.get(url, params=params, timeout=10)
response.raise_for_status()                      

# 5. Turn the JSON reply into a Python dictionary and print it
times = response.json()              
PRAYERS= {
    "Fajr": "fajr",
    "Dhuhr": "dhuhr",
    "Asr": "asr",
    "Maghrib": "magrib",
    "Isha": "isha"
}

print(f"Prayer times for {times['date']}")
for name, key in PRAYERS.items():
    print(f"{name:<8} {times[key]}")