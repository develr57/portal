from models.instruments import Instruments
from utils.repository import SQLAlchemyRepository
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import selectinload


class InstrumentsRepository(SQLAlchemyRepository):
    model = Instruments


    async def find_all_with_all(self):
        stmt = select(self.model).options(
            selectinload(self.model.company)
            .selectinload(self.model.department)
            .selectinload(self.model.inst_point)
            .selectinload(self.model.instr_type)
            .selectinload(self.model.manufacturer)
            .selectinload(self.model.object)
            .selectinload(self.model.status)
            .selectinload(self.model.storage)
            .selectinload(self.model.unit)
        )
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model_with_all() for row in res.all()]
        return res


    async def find_one_with_all(self, params: dict):
        stmt = select(self.model).options(
            selectinload(self.model.company)
            .selectinload(self.model.department)
            .selectinload(self.model.inst_point)
            .selectinload(self.model.instr_type)
            .selectinload(self.model.manufacturer)
            .selectinload(self.model.object)
            .selectinload(self.model.status)
            .selectinload(self.model.storage)
            .selectinload(self.model.unit)
        ).filter_by(**params)
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model_with_all()
        return res