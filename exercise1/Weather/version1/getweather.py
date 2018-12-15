import os
import pyowm
import json

api_key = os.environ.get('OPENWEATHER_API_KEY')
city = os.environ.get('CITY_NAME')
source = 'openweathermap'

observation = pyowm.OWM(api_key).weather_at_place(city)

forecast = json.loads(observation.get_weather().to_JSON())

weather = forecast['detailed_status']
temperature = forecast['temperature']['temp']
humidity = forecast['humidity']

output = 'source={}, city="{}", description="{}", temp={}, humidity={}'.format(source, city, weather, temperature, humidity)
print(output)
