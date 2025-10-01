from utils.unitofwork import IUnitOfWork
from schemas.units import UnitAddSchema, UnitEditSchema


class UnitsService:

    async def get_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.units.find_all()
            return res
    

    async def get_one(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.units.find_one(params=params)
            return res


    async def add(self, uow: IUnitOfWork, schema: UnitAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.units.add_one(res_dict)
            await uow.commit()
            return id
    

    async def edit(self, uow: IUnitOfWork, params: dict, schema: UnitEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.units.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.units.delete(params=params)
            await uow.commit()