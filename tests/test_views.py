from unittest import mock

from forecast import weather
from forecast.exceptions import CityNotFound
from forecast.utils import calculate_stats


class TestForecastView:
    def test_days_is_required_as_a_query_string(self, client):
        response = client.get("/api/locations/capetown/")

        assert response.status_code == 400
        assert response.json() == {
            "error": "`days` is a required query string parameter"
        }

    @mock.patch.object(weather, "get_daily_forecasts", side_effect=CityNotFound)
    def test_city_not_found_returns_400(self, mock_daily_forecasts, client):
        response = client.get("/api/locations/capetown/?days=3")

        assert response.status_code == 400
        assert response.json() == {"error": "`city` not found"}

    @mock.patch.object(weather, "get_daily_forecasts")
    def test_city_found_returns_forecast_stats(self, mock_daily_forecasts, client):
        forecasts = [20, 15, 20]
        mock_daily_forecasts.return_value = forecasts
        response = client.get("/api/locations/capetown/?days=3")

        assert response.status_code == 200
        assert response.json() == calculate_stats(forecasts)
