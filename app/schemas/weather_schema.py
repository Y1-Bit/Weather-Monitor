from pydantic import BaseModel


class WeatherDataModel(BaseModel):
    temperature: float
    wind_direction: str
    wind_speed: float
    pressure: float
    precipitation_type: str
    precipitation_amount: float


class WeatherDataModelList(BaseModel):
    weather_data: list[WeatherDataModel]
