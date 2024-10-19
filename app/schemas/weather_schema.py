from pydantic import BaseModel


class WeatherDataModel(BaseModel):
    """Model for representing weather data."""

    temperature: float  
    wind_direction: str  
    wind_speed: float  
    pressure: float  
    precipitation_type: str  
    precipitation_amount: float  


class WeatherDataModelList(BaseModel):
    """Model for representing a list of weather data records."""

    weather_data: list[WeatherDataModel]  
