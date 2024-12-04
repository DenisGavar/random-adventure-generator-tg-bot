import os
from dotenv import load_dotenv
import requests

load_dotenv(override=True)
API_BASE_URL = os.getenv("API_BASE_URL")

def fetch_categories():
    try:
        response = requests.get(f"{API_BASE_URL}/categories")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None
    
def register_user(data):
    try:
        response = requests.post(f"{API_BASE_URL}/users", json={key: value for key, value in data.items() if value is not None})
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None

def generate_task(data):
    try:
        response = requests.post(f"{API_BASE_URL}/tasks/generate", json={key: value for key, value in data.items() if value is not None})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None