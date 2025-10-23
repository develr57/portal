from utils.unitofwork import IUnitOfWork
from schemas.statuses import StatusAddSchema, StatusEditSchema


class StatusesService:

    async def get_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.statuses.find_all()
            return res
    

    async def get_one(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.statuses.find_one(params=params)
            return res


    async def add(self, uow: IUnitOfWork, schema: StatusAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.statuses.add_one(res_dict)
            await uow.commit()
            return id
    

    async def edit(self, uow: IUnitOfWork, params: dict, schema: StatusEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.statuses.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.statuses.delete(params=params)
            await uow.commit()