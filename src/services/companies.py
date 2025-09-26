import uuid
from utils.unitofwork import IUnitOfWork
from schemas.companies import CompanyAddSchema, CompanyEditSchema


class CompaniesService:

    async def get_companies(self, uow: IUnitOfWork):
        async with uow:
            companies = await uow.companies.find_all()
            return companies
    

    async def get_company(self, uow: IUnitOfWork, data: dict):
        async with uow:
            company = await uow.companies.find_one(data)
            return company


    async def add_company(self, uow: IUnitOfWork, schema: CompanyAddSchema) -> uuid.UUID:
        companies_dict = schema.model_dump()
        async with uow:
            id = await uow.companies.add_one(companies_dict)
            await uow.commit()
            return id
    

    async def edit_company(self, uow: IUnitOfWork, id: uuid.UUID, schema: CompanyEditSchema):
        companies_dict = schema.model_dump()
        async with uow:
            await uow.companies.edit_one(id, companies_dict)
            await uow.commit()


    async def delete_company(self, uow: IUnitOfWork, id: uuid.UUID):
        async with uow:
            await uow.companies.delete(id)
            await uow.commit()