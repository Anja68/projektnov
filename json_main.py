import json
import requests

def get_wheather_data():
    url = "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    json_data = response.json()
    return json_data


if __name__ == '__main__':
   weather_data = get_wheather_data()

   print(f"Weather in {weather_data['name']}")
   print(f"Wind speed {weather_data['wind']['speed']}")
   print(f"Wind direction {weather_data['wind']['deg']}°")

