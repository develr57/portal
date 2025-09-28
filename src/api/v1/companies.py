import uuid
from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.companies import CompanyAddSchema, CompanyEditSchema, CompanyResponseSchema
from services.companies import CompaniesService


router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await CompaniesService().get_companies(uow=uow)
    return res


@router.get(path="/{id}", response_model=CompanyResponseSchema)
async def get_one(id: uuid.UUID, uow: UOWDep):
    res = await CompaniesService().get_company(uow=uow, data=dict(id=id))
    return res


@router.post("")
async def add(schema: CompanyAddSchema, uow: UOWDep):
    id = await CompaniesService().add_company(uow=uow, schema=schema)
    return {"company_id": id}


@router.patch("/{id}")
async def edit(id: uuid.UUID, schema: CompanyEditSchema, uow: UOWDep):
    await CompaniesService().edit_company(uow=uow, id=id, schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: uuid.UUID, uow: UOWDep):
    await CompaniesService().delete_company(uow=uow, id=id)
    return {"ok": True}