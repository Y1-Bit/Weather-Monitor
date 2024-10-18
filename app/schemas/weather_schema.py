from pydantic import BaseModel


class WeatherDataModel(BaseModel):
    """Model for representing weather data."""

    temperature: float  # Current temperature in degrees Celsius
    wind_direction: str  # Wind direction as a string (e.g., "С", "ЮЗ")
    wind_speed: float  # Wind speed in meters per second
    pressure: float  # Atmospheric pressure in mm Hg
    precipitation_type: str  # Type of precipitation (e.g., "дождь", "снег")
    precipitation_amount: float  # Amount of precipitation in mm


class WeatherDataModelList(BaseModel):
    """Model for representing a list of weather data records."""

    weather_data: list[WeatherDataModel]  # List of WeatherDataModel instances
