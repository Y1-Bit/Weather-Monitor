from sqlalchemy import insert

from database.models.weater_data import WeatherData
from database.repo.base import BaseRepo
from schemas import WeatherDataModel


class WeatherDataRepo(BaseRepo):
    async def add_weather_data(self, weather_data: WeatherDataModel):
        insert_stmt = insert(WeatherData).values(
            temperature=weather_data.temperature,
            wind_direction=weather_data.wind_direction,
            wind_speed=weather_data.wind_speed,
            pressure=weather_data.pressure,
            precipitation_type=weather_data.precipitation_type,
            precipitation_amount=weather_data.precipitation_amount,
        )

        await self.session.execute(insert_stmt)
        await self.session.commit()
