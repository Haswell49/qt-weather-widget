import json

import requests


coords = (54.7116095, 20.46453)

API_KEY = "2941a123916dd70d540ccd0110ff800b"

uri_template = "https://api.openweathermap.org/data/2.5/weather?units=metric&lat={0}&lon={1}&appid={2}"

def get_weather_data():
    uri = uri_template.format(*coords, API_KEY)

    response = requests.get(uri)

    data = json.loads(response.content)

    return data["name"], \
           data["main"]["temp"], \
           data["main"]["humidity"], \
           data["rain"]["1h"] if "rain" in data.keys() else None, \
           data["wind"]["speed"]


print(get_weather_data())
