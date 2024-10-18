from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, TimestampMixin


class WeatherData(Base, TimestampMixin):
    """Model representing weather data records in the database."""
    
    __tablename__ = 'weather_data'  # Name of the table in the database

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    temperature: Mapped[float] = mapped_column(Float)
    wind_direction: Mapped[str] = mapped_column(String(3))
    wind_speed: Mapped[float] = mapped_column(Float)
    pressure: Mapped[float] = mapped_column(Float)
    precipitation_type: Mapped[str] = mapped_column(String(20))
    precipitation_amount: Mapped[float] = mapped_column(Float)
