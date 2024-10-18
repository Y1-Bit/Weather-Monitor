from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repo.weater_data import WeatherDataRepo


@dataclass
class RequestsRepo:
    """Repository for managing different database requests using an asynchronous session."""
    
    session: AsyncSession  # Asynchronous session for database operations

    @property
    def weather(self) -> WeatherDataRepo:
        """Property that provides access to the WeatherDataRepo.

        Returns:
            WeatherDataRepo: An instance of WeatherDataRepo to interact with weather data.
        """
        return WeatherDataRepo(self.session)  # Create and return an instance of WeatherDataRepo using the session
