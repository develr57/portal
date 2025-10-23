from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.companies import CompanyAddSchema, CompanyEditSchema, CompanyResponseSchema
from services.companies import CompaniesService


router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await CompaniesService().get_all(uow=uow)
    return res


@router.get(path="/{id}", response_model=CompanyResponseSchema)
async def get_one(id: int, uow: UOWDep):
    res = await CompaniesService().get_one(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: CompanyAddSchema, uow: UOWDep):
    id = await CompaniesService().add(uow=uow, schema=schema)
    return {"company_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: CompanyEditSchema, uow: UOWDep):
    await CompaniesService().edit(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await CompaniesService().delete(uow=uow, params=dict(id=id))
    return {"ok": True}