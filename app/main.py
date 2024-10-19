import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler  

from app.config import INTERVAL_MINUTES, LATITUDE, LONGITUDE, get_db_url  
from app.database.setup import create_engine, create_session_pool  
from app.services.weather_service import WeatherService 

logging.basicConfig(level=logging.INFO)


async def fetch_weather(weather_service: WeatherService):
    """Fetch and store weather data using the provided WeatherService instance."""
    try:
        await weather_service.fetch_and_store_weather(LATITUDE, LONGITUDE) 
        logging.info("Данные о погоде обновлены.")  
    except Exception as e:
        logging.error(f"Ошибка при обновлении данных о погоде: {e}")


async def main():
    """Main asynchronous function to set up the weather service and scheduler."""
    engine = create_engine(get_db_url(), echo=False)
    session_pool = create_session_pool(engine)
    weather_service = WeatherService(session_pool)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        fetch_weather, "interval", minutes=INTERVAL_MINUTES, args=[weather_service]
    )
    scheduler.start()  

    logging.info("Шедулер запущен. Ожидание задач...")  

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
