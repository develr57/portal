import uuid
from utils.unitofwork import IUnitOfWork
from schemas.manufacturers import ManufacturerAddSchema, ManufacturerEditSchema


class ManufacturersService:

    async def get_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.manufacturers.find_all()
            return res
    

    async def get_one(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.manufacturers.find_one(params=params)
            return res


    async def add(self, uow: IUnitOfWork, schema: ManufacturerAddSchema) -> uuid.UUID:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.manufacturers.add_one(res_dict)
            await uow.commit()
            return id
    

    async def edit(self, uow: IUnitOfWork, params: dict, schema: ManufacturerEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.manufacturers.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.manufacturers.delete(params=params)
            await uow.commit()