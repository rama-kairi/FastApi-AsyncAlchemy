from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_asyncalchemy import models


async def get_biggest_cities(session: AsyncSession) -> list[models.City]:
    result = await session.execute(
        select(models.City).order_by(models.City.population.desc()).limit(20)
    )
    return result.scalars().all()


def add_city(session: AsyncSession, name: str, population: int):
    new_city = models.City(name=name, population=population)
    session.add(new_city)
    return new_city
