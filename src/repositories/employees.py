from models.employees import Employees
from utils.repository import SQLAlchemyRepository
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import selectinload


class EmployeesRepository(SQLAlchemyRepository):
    model = Employees


    async def find_all_with_other(self):
        stmt = select(self.model).options(selectinload(self.model.company).selectinload(self.model.department))
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model_with_other() for row in res.all()]
        return res


    async def find_one_with_other(self, params: dict):
        stmt = select(self.model).options(selectinload(self.model.company).selectinload(self.model.department)).filter_by(**params)
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model_with_other()
        return res