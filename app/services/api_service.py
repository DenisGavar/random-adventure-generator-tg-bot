import os
from dotenv import load_dotenv
import requests

load_dotenv(override=True)
API_BASE_URL = os.getenv("API_BASE_URL")

def fetch_categories():
    try:
        url = f"{API_BASE_URL}/categories"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None
    
def register_user(data):
    try:
        url = f"{API_BASE_URL}/users"
        body = {key: value for key, value in data.items() if value is not None}
        response = requests.post(url, json = body)
        response.raise_for_status()
        return response, None
    except requests.exceptions.HTTPError as e:
        if response.status_code == 409:
            error_response = response.json()
            error_message = f"{error_response.get('error')}"
            return None, error_message
        else:
            print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
    
    return None, "Something went wrong. Please try again later."

def generate_new_task(data):
    try:
        url = f"{API_BASE_URL}/tasks/generate"
        body = {key: value for key, value in data.items() if value is not None}
        response = requests.post(url, json = body)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.HTTPError as e:
        if response.status_code == 429:
            error_response = response.json()
            error_message = f"{error_response.get('message')}\nYour limit: {error_response.get('limit')}"
            return None, error_message
        else:
            print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
    
    return None, "Something went wrong. Please try again later."
    
def get_existing_task(data):
    try:
        url = f"{API_BASE_URL}/tasks/get"
        body = {key: value for key, value in data.items() if value is not None}
        response = requests.post(url, json = body)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None
    
def fetch_tasks(data):
    try:
        url = f"{API_BASE_URL}/users/{data.get('telegram_id')}/tasks"
        if data['status']:
            url += f"?status={data.get('status')}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None

def complete_user_task(data):
    try:
        url = f"{API_BASE_URL}/tasks/{data.get('task_id')}/complete"
        body = {key: value for key, value in data.items() if key != 'task_id' and value is not None}
        response = requests.post(url, json = body)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
        return None