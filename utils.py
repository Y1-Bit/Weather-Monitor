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
