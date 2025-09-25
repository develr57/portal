from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.companies import CompanyCreateSchema, CompanyUpdateSchema
from services.companies import CompaniesService


router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get(path="")
async def get_all(uow: UOWDep):
    companies = await CompaniesService().get_companies(uow)
    return companies


@router.get(path="/{id}")
async def get_one(id: int, uow: UOWDep):
    company = await CompaniesService().get_company(uow, data=dict(id=id))
    return company


@router.post("")
async def add(company: CompanyCreateSchema, uow: UOWDep):
    company_id = await CompaniesService().add_company(uow, company)
    return {"company_id": company_id}


@router.patch("/{id}")
async def edit(id: int, company: CompanyUpdateSchema, uow: UOWDep):
    await CompaniesService().edit_company(uow, id, company)
    return {"ok": True}