from models.objects import Objects
from utils.repository import SQLAlchemyRepository
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import selectinload


class ObjectsRepository(SQLAlchemyRepository):
    model = Objects


    async def find_all_with_company(self):
        stmt = select(self.model).options(selectinload(self.model.company))
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model_with_company() for row in res.all()]
        return res


    async def find_one_with_company(self, params: dict):
        stmt = select(self.model).options(selectinload(self.model.company)).filter_by(**params)
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model_with_company()
        return res