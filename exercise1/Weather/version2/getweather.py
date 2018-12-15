import helpers.openweathermap as owm

def main():
    weather = owm.OWM()
    forecast = weather.get_forecast()

    # Get local values
    source = weather.source()
    location = weather.location()

    # Get values from open weather map
    status = weather.get_status(forecast)
    temp = weather.get_temperature(forecast)
    humidity = weather.get_humidity(forecast)

    # Print output
    output = 'source={}, city="{}", description="{}", temp={}, humidity={}'.format(source, location, status, temp, humidity)
    print(output)
    return

if __name__ == '__main__':
    main()
