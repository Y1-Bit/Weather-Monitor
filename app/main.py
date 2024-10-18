import asyncio

from app.config import LATITUDE, LONGITUDE, get_db_url
from app.database.setup import create_engine, create_session_pool
from app.services.data_service import DataExportService
from app.services.weather_service import WeatherService


async def main():
    engine = create_engine(get_db_url(), echo=True)
    session_pool = create_session_pool(engine)
    weather_service = WeatherService(session_pool)
    data_export_service = DataExportService(weather_service)

    await data_export_service.export_latest_weather_data_to_xlsx("data.xlsx")


if __name__ == "__main__":
    asyncio.run(main())
