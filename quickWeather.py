# PROJECT : FETCHING CURRENT WEATHER DATA


# MODULE
import json
import requests
import sys


# SOURCE : OpenWeatherMap.org


# PREPARE THE DATA
url = 'https://samples.openweathermap.org/data/2.5/forecast/daily?id=524901&appid=b1b15e88fa797225412429c1c50c122a1'
response = requests.get(url)
print(response.status_code)
print(response.text)


# LOAD DATA JSON INTO PYTHON
JSON_data = json.loads(response.text)
print(JSON_data)


# SCRAPE DATA
print(JSON_data['city']['name'])

for forecast in JSON_data['list']:
    print(forecast['weather'])

print()
w = JSON_data['list']
print('Currrent weather in :'+(JSON_data['city']['name']))

print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'],'-',w[2]['weather'][0]['description'])
