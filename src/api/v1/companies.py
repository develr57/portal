import uuid
from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.companies import CompanyAddSchema, CompanyEditSchema
from services.companies import CompaniesService


router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get(path="")
async def get_all(uow: UOWDep):
    companies = await CompaniesService().get_companies(uow)
    return companies


@router.get(path="/{id}")
async def get_one(id: uuid.UUID, uow: UOWDep):
    company = await CompaniesService().get_company(uow, dict(id=id))
    return company


@router.post("")
async def add(schema: CompanyAddSchema, uow: UOWDep):
    id = await CompaniesService().add_company(uow, schema)
    return {"company_id": id}


@router.patch("/{id}")
async def edit(id: uuid.UUID, schema: CompanyEditSchema, uow: UOWDep):
    await CompaniesService().edit_company(uow, id, schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: uuid.UUID, uow: UOWDep):
    await CompaniesService().delete_company(uow=uow, id=id)
    return {"ok": True}