import openmeteo_requests
import requests_cache
from openmeteo_sdk.WeatherApiResponse import WeatherApiResponse
from retry_requests import retry

from config import LATITUDE, LONGITUDE
from utils import (
    convert_pressure_to_mm_hg,
    convert_wind_direction,
    get_precipitation_info,
)


def fetch_weather_data(latitude: float, longitude: float):
    cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "precipitation",
            "rain",
            "showers",
            "snowfall",
            "surface_pressure",
            "wind_speed_10m",
            "wind_direction_10m",
        ],
        "wind_speed_unit": "ms",
    }

    responses = openmeteo.weather_api(url, params=params)
    return responses[0]


def get_current_weather(current_data: WeatherApiResponse):
    current = current_data.Current()
    if current is None:
        raise ValueError("Weather data not fetched. Call 'fetch_weather_data()' first.")

    return {
        "temperature": current.Variables(0).Value(),
        "wind_speed": current.Variables(6).Value(),
        "wind_direction": convert_wind_direction(current.Variables(7).Value()),
        "pressure": convert_pressure_to_mm_hg(current.Variables(5).Value()),
        "precipitation": current.Variables(1).Value(),
        "precipitation_type": get_precipitation_info(
            current.Variables(4).Value(),
            current.Variables(2).Value(),
            current.Variables(3).Value(),
        ),
    }


if __name__ == "__main__":
    current_data = fetch_weather_data(LATITUDE, LONGITUDE)
    current_weather = get_current_weather(current_data)

    print("Текущая погода:")
    print(f"Температура: {current_weather['temperature']}°C")
    print(f"Скорость ветра: {current_weather['wind_speed']} м/с")
    print(f"Направление ветра: {current_weather['wind_direction']}")
    print(f"Давление: {current_weather['pressure']} мм рт. ст.")
    print(f"Тип осадков: {current_weather['precipitation_type']}")
    print(f"Количество осадков: {current_weather['precipitation']} мм")
