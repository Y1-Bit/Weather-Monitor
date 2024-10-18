import asyncio
import logging

from app.config import get_db_url  # Function to retrieve database connection URL
from app.database.setup import create_engine, create_session_pool  # Functions for database setup
from app.misc.utils import export_latest_weather_data_to_xlsx  # Utility for exporting data to Excel
from app.services.weather_service import WeatherService  # Weather service for data operations

# Configure logging to display information and error messages
logging.basicConfig(level=logging.INFO)


async def main():
    """Main asynchronous function to fetch and export weather data."""
    try:
        # Create the database engine using the connection URL
        engine = create_engine(get_db_url(), echo=False)
        # Create a session pool for interacting with the database
        session_pool = create_session_pool(engine)
        # Instantiate the WeatherService with the session pool
        weather_service = WeatherService(session_pool)

        # Fetch the latest weather data
        data = await weather_service.get_latest_weather_data()

        # Export the fetched weather data to an Excel file
        export_latest_weather_data_to_xlsx(data, "data/latest_weather_data.xlsx")
        logging.info("Экспорт данных завершён.")  # Log successful export

    except Exception as e:
        # Log any exceptions that occur during execution
        logging.error(f"Ошибка при экспорте данных: {e}")


if __name__ == "__main__":
    # Run the main asynchronous function
    asyncio.run(main())
