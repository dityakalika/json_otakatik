# PROJECT : FETCHING CURRENT WEATHER DATA

# MODULE

import json
import requests
import sys

# SOURCE : OpenWeatherMap.org

url = 'https://samples.openweathermap.org/data/2.5/forecast/daily?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
response = requests.get(url)
print(response.status_code)
print(response.text)

JSON_data = json.loads(response.text)
print(JSON_data)


print(JSON_data['city']['name'])

for forecast in JSON_data['list']:
    print(forecast['weather'])

