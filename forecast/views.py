from http import HTTPStatus

from django.http import JsonResponse

from forecast import weather
from forecast.exceptions import CityNotFound
from forecast.utils import calculate_stats


def forecast_view(request, city):
    days = request.GET.get("days")
    if not days:
        return JsonResponse(
            {"error": "`days` is a required query string parameter"},
            status=HTTPStatus.BAD_REQUEST,
        )
    try:
        forecast = weather.get_daily_forecasts(city, days)
    except CityNotFound:
        return JsonResponse(
            {"error": "`city` not found"}, status=HTTPStatus.BAD_REQUEST
        )

    stats = calculate_stats(forecast)
    return JsonResponse(stats)
