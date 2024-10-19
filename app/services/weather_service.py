from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio.session import async_sessionmaker

from app.apis.weather_api import fetch_weather_data, get_current_weather
from app.database.repo.requests import RequestsRepo


@dataclass
class WeatherService:
    """Service for fetching and storing weather data."""
    
    session_pool: async_sessionmaker[AsyncSession]  

    async def fetch_and_store_weather(self, latitude: float, longitude: float):
        """Fetch weather data from the API and store it in the database.

        Args:
            latitude (float): Latitude for the weather data.
            longitude (float): Longitude for the weather data.
        """
        weather_data = fetch_weather_data(latitude, longitude)
        
        current_weather = get_current_weather(weather_data)

        async with self.session_pool() as session:
            repo = RequestsRepo(session)  
            await repo.weather.add_weather_data(current_weather)  

    async def get_latest_weather_data(self):
        """Retrieve the latest weather data from the database.

        Returns:
            WeatherDataModelList: List of the latest weather data records.
        """
        async with self.session_pool() as session:
            repo = RequestsRepo(session)  
            data = await repo.weather.get_latest_weather_data(10)  
        return data  
