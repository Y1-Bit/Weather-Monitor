from app.database.models.weater_data import WeatherData
from app.database.repo.base import BaseRepo
from sqlalchemy import insert, select

from app.schemas.weather_schema import WeatherDataModel, WeatherDataModelList


class WeatherDataRepo(BaseRepo):
    """Repository for interacting with the WeatherData model in the database."""
    
    async def add_weather_data(self, weather_data: WeatherDataModel):
        """Add a new weather data record to the database.

        Args:
            weather_data (WeatherDataModel): The weather data to be added.
        """
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

    async def get_latest_weather_data(self, limit: int = 10) -> WeatherDataModelList:
        """Retrieve the latest weather data records from the database.

        Args:
            limit (int): The maximum number of records to retrieve (default is 10).

        Returns:
            WeatherDataModelList: A list of the latest weather data records.
        """
        query = select(WeatherData).order_by(WeatherData.created_at.desc()).limit(limit)
        
        result = await self.session.execute(query)
        weather_data_objects = result.scalars().all()

        return WeatherDataModelList(
            weather_data=[
                WeatherDataModel(
                    temperature=data.temperature,
                    wind_direction=data.wind_direction,
                    wind_speed=data.wind_speed,
                    pressure=data.pressure,
                    precipitation_type=data.precipitation_type,
                    precipitation_amount=data.precipitation_amount,
                )
                for data in weather_data_objects
            ]
        )
