import os
import requests
from dotenv import load_dotenv

load_dotenv()

ANIMALS_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")

def fetch_data(animal_name):
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}
    res = requests.get(ANIMALS_URL, headers=headers, params=params)
    return res.json()