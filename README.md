## Forecast Stats API (using python 3.9)

# To get a weather API key
Go to https://www.weatherapi.com/signup.aspx and sign up. Note your API key

# To run API
```bash
export WEATHER_FORECAST_API_KEY=yourkey
pip install -r requirements.txt
python manage.py runserver
open http://127.0.0.1:8000/api/locations/capetown/?days=3
```

# To run tests
```bash
pip install -r requirements.txt
pytest
```