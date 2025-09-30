from utils.unitofwork import IUnitOfWork
from schemas.types import TypeAddSchema, TypeEditSchema


class TypesService:

    async def get_types(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.types.find_all()
            return res
    

    async def get_type(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.types.find_one(params=params)
            return res


    async def add_type(self, uow: IUnitOfWork, schema: TypeAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.types.add_one(res_dict)
            await uow.commit()
            return id
    

    async def edit_type(self, uow: IUnitOfWork, params: dict, schema: TypeEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.types.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete_type(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.types.delete(params=params)
            await uow.commit()