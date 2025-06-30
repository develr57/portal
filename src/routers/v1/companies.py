from fastapi import APIRouter
from src.routers.dependencies import UOWDep
from src.schemas.companies import CompanySchemaBase, CompanySchemaAdd, CompanySchemaEdit
from src.services.companies import CompaniesService


router = APIRouter(prefix="/companies", tags=["companies"])


@router.get(path="")
async def get_all(uow: UOWDep):
    companies = CompaniesService.get_companies(uow=uow)
    return companies


@router.get(path="/{id}")
async def get_one(id: int, uow: UOWDep):
    company = CompaniesService.get_company(uow=uow, data=dict(id=id))
    return company


@router.post("")
async def add(company: CompanySchemaAdd, uow: UOWDep):
    company_id = await CompaniesService().add_company(uow, company)
    return {"company_id": company_id}


@router.patch("/{id}")
async def edit(id: int, company: CompanySchemaEdit, uow: UOWDep):
    await CompaniesService().edit_company(uow, id, company)
    return {"ok": True}