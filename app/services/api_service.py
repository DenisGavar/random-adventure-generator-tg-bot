import os
from dotenv import load_dotenv
import requests

load_dotenv(override=True)
API_BASE_URL = os.getenv("API_BASE_URL")

def fetch_categories():
    try:
        print("start")
        response = requests.get(f"{API_BASE_URL}/categories")
        print("got")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None