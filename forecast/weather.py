import requests

from config.settings import (
    WEATHER_FORECAST_API_KEY,
    WEATHER_FORECAST_API_TIMEOUT,
    WEATHER_FORECAST_API_URL,
)
from forecast.exceptions import CityNotFound


def get_daily_forecasts(city, days):
    payload = {"key": WEATHER_FORECAST_API_KEY, "q": city, "days": days}
    r = requests.get(
        WEATHER_FORECAST_API_URL, params=payload, timeout=WEATHER_FORECAST_API_TIMEOUT
    )
    if r.status_code == 400:
        raise CityNotFound()
    r.raise_for_status()
    daily_forecasts = r.json()["forecast"]["forecastday"]
    avg_daily_forecasts = [forecast["day"]["avgtemp_c"] for forecast in daily_forecasts]
    return avg_daily_forecasts
