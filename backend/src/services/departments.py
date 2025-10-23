from utils.unitofwork import IUnitOfWork
from schemas.departments import DepartmentAddSchema, DepartmentEditSchema


class DepartmentsService:

    async def get_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.departments.find_all()
            return res


    async def get_all_with_company(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.departments.find_all_with_company()
            return res


    async def get_one(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.departments.find_one(params=params)
            return res


    async def get_one_with_company(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.departments.find_one_with_company(params=params)
            return res


    async def add(self, uow: IUnitOfWork, schema: DepartmentAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.departments.add_one(res_dict)
            await uow.commit()
            return id


    async def edit(self, uow: IUnitOfWork, params: dict, schema: DepartmentEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.departments.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.departments.delete(params=params)
            await uow.commit()
