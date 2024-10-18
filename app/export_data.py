import asyncio
import logging

from app.config import get_db_url
from app.database.setup import create_engine, create_session_pool
from app.misc.utils import export_latest_weather_data_to_xlsx
from app.services.weather_service import WeatherService

logging.basicConfig(level=logging.INFO)


async def main():
    try:
        engine = create_engine(get_db_url(), echo=False)
        session_pool = create_session_pool(engine)
        weather_service = WeatherService(session_pool)
        data = await weather_service.get_latest_weather_data()

        export_latest_weather_data_to_xlsx(data, "data/latest_weather_data.xlsx")
        logging.info("Экспорт данных завершён.")

    except Exception as e:
        logging.error(f"Ошибка при экспорте данных: {e}")


if __name__ == "__main__":
    asyncio.run(main())
