from utils.unitofwork import IUnitOfWork
from schemas.storages import StorageAddSchema, StorageEditSchema


class StoragesService:

    async def get_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.storages.find_all()
            return res


    async def get_all_with_dept(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.storages.find_all_with_dept()
            return res


    async def get_one(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.storages.find_one(params=params)
            return res


    async def get_one_with_dept(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.storages.find_one_with_dept(params=params)
            return res


    async def add(self, uow: IUnitOfWork, schema: StorageAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.storages.add_one(res_dict)
            await uow.commit()
            return id


    async def edit(self, uow: IUnitOfWork, params: dict, schema: StorageEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.storages.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.storages.delete(params=params)
            await uow.commit()
