from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repo.weater_data import WeatherDataRepo


@dataclass
class RequestsRepo:

    session: AsyncSession

    @property
    def weather(self) -> WeatherDataRepo:
        return WeatherDataRepo(self.session)
