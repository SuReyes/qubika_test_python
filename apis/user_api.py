from playwright.sync_api import sync_playwright
import requests


def create_user(username: str, password: str):
    # Step 1: Create a new user via the API
    base_url = "https://api.club-administration.qa.qubika.com"
    api_url = '/api/auth/register'  # Replace with your actual API endpoint
    user_data = {
              "email": username,
              "password": password,
              "roles": [
                "ROLE_ADMIN"
              ]
            }

    # Send POST request to create a user
    response = requests.post(base_url+api_url, json=user_data)

    # Check if the user was created successfully
    return response.status_code, response.json()
