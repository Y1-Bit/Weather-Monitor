from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from app.apis.weather_api import fetch_weather_data, get_current_weather
from app.database.repo.requests import RequestsRepo


@dataclass
class WeatherService:
    session_pool: async_sessionmaker[AsyncSession]

    async def fetch_and_store_weather(self, latitude: float, longitude: float):
        weather_data = fetch_weather_data(latitude, longitude)
        current_weather = get_current_weather(weather_data)

        async with self.session_pool() as session:
            repo = RequestsRepo(session)
            await repo.weather.add_weather_data(current_weather)

    async def get_latest_weather_data(self):
        async with self.session_pool() as session:
            repo = RequestsRepo(session)
            data = await repo.weather.get_latest_weather_data(10)
        return data
