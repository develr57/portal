from src.utils.unitofwork import IUnitOfWork
from src.schemas.companies import CompanySchemaBase, CompanySchemaAdd, CompanySchemaEdit


class CompaniesService:

    async def get_companies(self, uow: IUnitOfWork):
        async with uow:
            companies = await uow.companies.find_all()
            return companies
    

    async def get_company(self, uow: IUnitOfWork, data: dict):
        async with uow:
            company = await uow.companies.find_one(data)
            return company


    async def add_company(self, uow: IUnitOfWork, company: CompanySchemaAdd):
        companies_dict = company.model_dump()
        async with uow:
            company_id = await uow.companies.add_one(companies_dict)
            await uow.commit()
            return company_id
    

    async def edit_company(self, uow: IUnitOfWork, company_id: int, company: CompanySchemaEdit):
        companies_dict = company.model_dump()
        async with uow:
            await uow.companies.edit_one(company_id, companies_dict)
            await uow.commit()