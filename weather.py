import os
import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_by_zip(zip_code, country_code='US'):
    weather_key = os.getenv('OPENWEATHER_API_KEY')
    url = f"{BASE_URL}?zip={zip_code},{country_code}&appid={weather_key}"
    response = requests.get(url)

    # check if the request was successful
    if response.status_code == 200:
        weather_data = response.json()
        print(weather_data)
        return weather_data
    else:
        response.raise_for_status()

