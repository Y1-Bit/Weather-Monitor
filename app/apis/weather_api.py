import openmeteo_requests
import requests_cache
from openmeteo_sdk.WeatherApiResponse import WeatherApiResponse
from retry_requests import retry

from app.config import LATITUDE, LONGITUDE
from app.schemas.weather_schema import WeatherDataModel
from app.misc.utils import (
    convert_pressure_to_mm_hg,
    convert_wind_direction,
    get_precipitation_info,
)


def fetch_weather_data(latitude: float, longitude: float) -> WeatherApiResponse:
    """Fetch weather data from the Open Meteo API for the given latitude and longitude."""
    # Create a cached session with an expiration time of 1 hour
    cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
    # Wrap the cached session with retry functionality
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    # Initialize Open Meteo client
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Define the API endpoint and parameters for the weather forecast
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

    # Fetch the weather data using the defined parameters
    responses = openmeteo.weather_api(url, params=params)
    return responses[0]  # Return the first response


def get_current_weather(current_data: WeatherApiResponse) -> WeatherDataModel:
    """Extract current weather information from the API response."""
    current = current_data.Current()
    
    # Raise an error if current weather data is not available
    if current is None:
        raise ValueError("Weather data not fetched. Call 'fetch_weather_data()' first.")

    # Create a WeatherDataModel object with relevant weather details
    return WeatherDataModel(
        temperature=current.Variables(0).Value(),  # Temperature in °C
        wind_speed=current.Variables(6).Value(),   # Wind speed in m/s
        wind_direction=convert_wind_direction(current.Variables(7).Value()),  # Converted wind direction
        pressure=convert_pressure_to_mm_hg(current.Variables(5).Value()),  # Pressure in mm Hg
        precipitation_amount=current.Variables(1).Value(),  # Precipitation amount in mm
        precipitation_type=get_precipitation_info(
            current.Variables(4).Value(),  # Snowfall value
            current.Variables(2).Value(),   # Rain value
            current.Variables(3).Value(),   # Showers value
        ),
    )


if __name__ == "__main__":
    # Fetch current weather data using the specified latitude and longitude
    current_data = fetch_weather_data(LATITUDE, LONGITUDE)
    current_weather = get_current_weather(current_data)

    # Print the current weather information to the console
    print("Текущая погода:")
    print(f"Температура: {current_weather.temperature}°C")
    print(f"Скорость ветра: {current_weather.wind_speed} м/с")
    print(f"Направление ветра: {current_weather.wind_direction}")
    print(f"Давление: {current_weather.pressure} мм рт. ст.")
    print(f"Тип осадков: {current_weather.precipitation_type}")
    print(f"Количество осадков: {current_weather.precipitation_amount} мм")
