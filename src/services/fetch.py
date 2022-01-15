import requests
from utils.constants import BASE_URL

def api_service(base, endpoint):
    response = requests.get(base + endpoint)
    return response.json()

def dolar_blue():
    return api_service(BASE_URL, "dolarblue")

def dolar_oficial():
    return api_service(BASE_URL, "dolaroficial")