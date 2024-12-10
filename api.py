
from exceptions import APIError
import requests


API_KEY = "qDljHMNmC8wqtYkWqbqjmYy5yGEYNonE"

def get_weather(city: str) -> tuple[float, float, float, float]:

    try:
        data = requests.get(
            "http://dataservice.accuweather.com/locations/v1/cities/search", 
            params=dict(apikey=API_KEY, q=city, details=True),
            ).json()
        location_key = data[0].get("Key")
    except IndexError:
        raise APIError(f"Не удалось найти город {city}")
    except Exception:
        raise APIError(f"Неизвестаня ошибка при получении города {city}")

    try:
        data = requests.get(
            f"http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{location_key}",
            params=dict(apikey=API_KEY, details=True, metric=True),
            ).json()
    except Exception:
        raise APIError(f"Не удалось получить погоду города {city}")
    
    try:
        weather = (
            data[0]["Temperature"]["Value"],
            data[0]["RelativeHumidity"],
            data[0]["Wind"]["Speed"]["Value"],
            data[0]["RainProbability"],
        )
        return weather
    except Exception:
        raise APIError(f"Не удалось распаковать погоду города {city}")