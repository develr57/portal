from utils.unitofwork import IUnitOfWork
from schemas.employees import EmployeeAddSchema, EmployeeEditSchema


class EmployeesService:

    async def get_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.employees.find_all()
            return res


    async def get_all_with_other(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.employees.find_all_with_other()
            return res


    async def get_one(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.employees.find_one(params=params)
            return res


    async def get_one_with_other(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.employees.find_one_with_other(params=params)
            return res


    async def add(self, uow: IUnitOfWork, schema: EmployeeAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.employees.add_one(res_dict)
            await uow.commit()
            return id


    async def edit(self, uow: IUnitOfWork, params: dict, schema: EmployeeEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.employees.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.employees.delete(params=params)
            await uow.commit()
