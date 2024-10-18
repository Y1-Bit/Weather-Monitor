import logging
from dataclasses import dataclass
from pathlib import Path

import openpyxl

from app.services.weather_service import WeatherService


@dataclass
class DataExportService:
    weather_service: WeatherService

    async def export_latest_weather_data_to_xlsx(self, file_path: str):
        latest_weather_data = await self.weather_service.get_latest_weather_data()

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Latest Weather Data"

        headers = [
            "Temperature",
            "Wind Direction",
            "Wind Speed",
            "Pressure",
            "Precipitation Type",
            "Precipitation Amount",
        ]
        ws.append(headers)

        for weather in latest_weather_data.weather_data:
            ws.append(
                [
                    weather.temperature,
                    weather.wind_direction,
                    weather.wind_speed,
                    weather.pressure,
                    weather.precipitation_type,
                    weather.precipitation_amount,
                ]
            )

        save_path = Path(file_path)
        wb.save(save_path)
        logging.info(f"Weather data exported to {save_path}")
