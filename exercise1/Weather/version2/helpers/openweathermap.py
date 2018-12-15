import pyowm
import json
import sys
from .config import get_env

def string_to_json(func):
    """
    :param func:
    :return: dict
    """
    def wrapper(self, *args, **kwargs):
        parsed = json.loads(func(self, *args, **kwargs))
        return parsed
    return wrapper

class OWM(object):

    def __init__(self, api_key=get_env()['api_key'], city=get_env()['city']):
        self.__city = city
        self.__owm = pyowm.OWM(api_key)
        self.__source = 'openweathermap'

    def source(self):
        """
        :return: str
        """
        return self.__source

    def location(self):
        """
        :return: str
        """
        return self.__city

    def __observation(self):
        """
        :return: object
        """
        observation = self.__owm.weather_at_place(self.__city)
        return observation

    @string_to_json
    def get_forecast(self):
        """
        :return: str
        """
        try:
            forecast_output = self.__observation().get_weather()
        except Exception as e:
            print(e)
            sys.exit(1)
        else:
            forecast = forecast_output.to_JSON()
        return forecast

    def get_status(self, forecast):
        """
        :param forecast: dict
        :return: str
        """
        weather = forecast['detailed_status']
        return weather

    def get_temperature(self, forecast):
        """
        :param forecast: dict
        :return: str
        """
        temperature = forecast['temperature']['temp']
        return temperature

    def get_humidity(self, forecast):
        """
        :param forecast: dict
        :return: str
        """
        humidity = forecast['humidity']
        return humidity
