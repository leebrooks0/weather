import requests

from config.settings import WEATHER_FORECAST_API_KEY, WEATHER_FORECAST_API_TIMEOUT, WEATHER_FORECAST_API_URL



def get_temperature(city, days):
    payload = {'key': WEATHER_FORECAST_API_KEY, 'q': city, 'days': days}
    r = requests.get(WEATHER_FORECAST_API_URL, params=payload, timeout=WEATHER_FORECAST_API_TIMEOUT)
    r.raise_for_status()
    daily_forecasts = r.json()["forecast"]["forecastday"]
    avg_daily_forecasts = [forecast["day"]["avgtemp_c"] for forecast in daily_forecasts]
    return avg_daily_forecasts

# get_temperature("capeddd", 2)
# {'error': {'code': 1006, 'message': 'No matching location found.'}}

# CityNotFoundException

# get_temperature(None, None)
# {'error': {'code': 1003, 'message': 'Parameter q is missing.'}}
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "/Users/lee.brooks/PycharmProjects/weather/forecast/weather.py", line 11, in get_temperature
#     r.raise_for_status()
#   File "/Users/lee.brooks/PycharmProjects/weather/venv/lib/python3.8/site-packages/requests/models.py", line 953, in raise_for_status
#     raise HTTPError(http_error_msg, response=self)
# requests.exceptions.HTTPError: 400 Client Error: Bad Request for url: https://api.weatherapi.com/v1/forecast.json?key=dcc289b615464d91a7f174755211211
