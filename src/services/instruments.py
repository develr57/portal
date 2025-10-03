from utils.unitofwork import IUnitOfWork
from schemas.instruments import InstrumentAddSchema, InstrumentEditSchema


class InstrumentsService:

    async def get_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.instruments.find_all()
            return res


    async def get_all_with_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.instruments.find_all_with_all()
            return res


    async def get_one(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.instruments.find_one(params=params)
            return res


    async def get_one_with_all(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.instruments.find_one_with_all(params=params)
            return res


    async def add(self, uow: IUnitOfWork, schema: InstrumentAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.instruments.add_one(res_dict)
            await uow.commit()
            return id


    async def edit(self, uow: IUnitOfWork, params: dict, schema: InstrumentEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.instruments.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.instruments.delete(params=params)
            await uow.commit()
