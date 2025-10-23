from utils.unitofwork import IUnitOfWork
from schemas.companies import CompanyAddSchema, CompanyEditSchema


class CompaniesService:

    async def get_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.companies.find_all()
            return res
    

    async def get_one(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.companies.find_one(params=params)
            return res


    async def add(self, uow: IUnitOfWork, schema: CompanyAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.companies.add_one(res_dict)
            await uow.commit()
            return id
    

    async def edit(self, uow: IUnitOfWork, params: dict, schema: CompanyEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.companies.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.companies.delete(params=params)
            await uow.commit()