from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from database.repo.requests import RequestsRepo
from weather_api import fetch_weather_data, get_current_weather


@dataclass
class WeatherService:
    session_pool: async_sessionmaker[AsyncSession]

    async def fetch_and_store_weather(self, latitude: float, longitude: float):
        async with self.session_pool() as session:
            weather_data = fetch_weather_data(latitude, longitude)
            current_weather = get_current_weather(weather_data)

            repo = RequestsRepo(session)
            await repo.weather.add_weather_data(current_weather)
