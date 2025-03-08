import requests
from typing import Any, Dict, List

def get_resp(url:str = "http://0.0.0.0:8000/status") -> dict[str, Any]: 

    try:
        response = requests.get(url)
        response.raise_for_status() 

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except ValueError:
        return "Failed to decode JSON response"