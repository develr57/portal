from utils.unitofwork import IUnitOfWork
from schemas.instr_types import InstrTypeAddSchema, InstrTypeEditSchema


class InstrTypesService:

    async def get_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.instr_types.find_all()
            return res
    

    async def get_one(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.instr_types.find_one(params=params)
            return res


    async def add(self, uow: IUnitOfWork, schema: InstrTypeAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.instr_types.add_one(res_dict)
            await uow.commit()
            return id
    

    async def edit(self, uow: IUnitOfWork, params: dict, schema: InstrTypeEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.instr_types.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.instr_types.delete(params=params)
            await uow.commit()