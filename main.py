import asyncio

from config import LATITUDE, LONGITUDE
from database.repo.requests import RequestsRepo
from database.setup import create_engine, create_session_pool
from services.weather_service import WeatherService


async def main():
    engine = create_engine("", echo=True)
    session_pool = create_session_pool(engine)
    weather_service = WeatherService(session_pool)
    await weather_service.fetch_and_store_weather(
        latitude=LATITUDE, longitude=LONGITUDE
    )


if __name__ == "__main__":
    asyncio.run(main())
