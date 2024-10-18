from pathlib import Path

import openpyxl
import pandas as pd

from app.schemas.weather_schema import WeatherDataModelList


def convert_wind_direction(degrees: float) -> str:
    directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
    index = round(degrees / 45) % 8
    return directions[index]


def convert_pressure_to_mm_hg(surface_pressure: float) -> float:
    return surface_pressure * 0.75006


def get_precipitation_info(
    current_snowfall: float, current_rain: float, current_showers: float
) -> str:
    if current_snowfall > 0:
        precipitation_type = "снег"
    elif current_rain > 0 or current_showers > 0:
        precipitation_type = "дождь"
    else:
        precipitation_type = "нет осадков"

    return precipitation_type


def export_weather_data(weather_data: dict, file_name="weather_data.xlsx"):
    df = pd.DataFrame([weather_data])
    df.to_excel(file_name, index=False)


def export_latest_weather_data_to_xlsx(
    latest_weather_data: WeatherDataModelList, file_path: str
):
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
