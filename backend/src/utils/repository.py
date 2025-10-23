import uuid
from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict) -> int:
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> list:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def edit_one(self, params: dict, data: dict) -> int:
        stmt = update(self.model).values(**data).filter_by(**params).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def find_one(self, params: dict):
        stmt = select(self.model).filter_by(**params)
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model()
        return res

    async def delete(self, params: dict):
        stmt = delete(self.model).filter_by(**params)
        res = await self.session.execute(stmt)
        return res