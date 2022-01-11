import requests

base_url = "https://api.gastonotero.com/"

def apiService(base, endpoint):
    response = requests.get(base + endpoint)
    return response.json()

def dolarBlue():
    return apiService(base_url, "dolarblue")