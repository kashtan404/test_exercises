import os

def get_env():
    """
    :return: dict
    """
    config = dict()
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    if api_key is not None:
        config['api_key'] = api_key
    else:
        raise ValueError('Environment "OPENWEATHER_API_KEY" is not defined')

    city = os.environ.get('CITY_NAME')
    if city is not None:
        config['city'] = city
    else:
        raise ValueError('Environment "CITY_NAME" is not defined')

    return config
