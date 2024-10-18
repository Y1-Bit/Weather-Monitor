import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler  # Import the asynchronous scheduler

from app.config import INTERVAL_MINUTES, LATITUDE, LONGITUDE, get_db_url  # Import configuration settings
from app.database.setup import create_engine, create_session_pool  # Import database setup functions
from app.services.weather_service import WeatherService  # Import the weather service

# Configure logging to display information and error messages
logging.basicConfig(level=logging.INFO)


async def fetch_weather(weather_service: WeatherService):
    """Fetch and store weather data using the provided WeatherService instance."""
    try:
        await weather_service.fetch_and_store_weather(LATITUDE, LONGITUDE)  # Fetch and store weather data
        logging.info("Данные о погоде обновлены.")  # Log success message
    except Exception as e:
        # Log any exceptions that occur during the weather fetching process
        logging.error(f"Ошибка при обновлении данных о погоде: {e}")


async def main():
    """Main asynchronous function to set up the weather service and scheduler."""
    # Create the database engine using the connection URL
    engine = create_engine(get_db_url(), echo=False)
    # Create a session pool for interacting with the database
    session_pool = create_session_pool(engine)
    # Instantiate the WeatherService with the session pool
    weather_service = WeatherService(session_pool)

    # Create an asynchronous scheduler
    scheduler = AsyncIOScheduler()
    # Schedule the fetch_weather function to run at specified intervals
    scheduler.add_job(
        fetch_weather, "interval", minutes=INTERVAL_MINUTES, args=[weather_service]
    )
    scheduler.start()  # Start the scheduler

    logging.info("Шедулер запущен. Ожидание задач...")  # Log that the scheduler is running

    # Keep the event loop running to continue scheduling jobs
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    # Get the event loop and run the main asynchronous function
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
