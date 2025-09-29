import uuid
from utils.unitofwork import IUnitOfWork
from schemas.objects import ObjectAddSchema, ObjectEditSchema


class ObjectsService:

    async def get_objects(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.objects.find_all()
            return res


    async def get_objects_with_company(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.objects.find_all_with_company()
            return res
    

    async def get_object(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.objects.find_one(params=params)
            return res


    async def get_object_with_company(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.objects.find_one_with_company(params=params)
            return res


    async def add_object(self, uow: IUnitOfWork, schema: ObjectAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.objects.add_one(res_dict)
            await uow.commit()
            return id
    

    async def edit_object(self, uow: IUnitOfWork, params: dict, schema: ObjectEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.objects.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete_object(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.objects.delete(params=params)
            await uow.commit()