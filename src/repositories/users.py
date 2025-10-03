from models.users import Users
from utils.repository import SQLAlchemyRepository
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import selectinload


class UsersRepository(SQLAlchemyRepository):
    model = Users


    async def find_all_with_emp(self):
        stmt = select(self.model).options(selectinload(self.model.employee))
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model_with_emp() for row in res.all()]
        return res


    async def find_one_with_emp(self, params: dict):
        stmt = select(self.model).options(selectinload(self.model.employee)).filter_by(**params)
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model_with_emp()
        return res