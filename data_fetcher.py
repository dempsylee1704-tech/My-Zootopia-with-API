import requests

API_KEY = "bgjuxHDk4fMnA7otei0N8RUWoliZMxz9PjJ7F0ZB"

ANIMALS_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}
    res = requests.get(ANIMALS_URL, headers=headers, params=params)
    return res.json()