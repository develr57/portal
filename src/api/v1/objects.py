from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.objects import ObjectAddSchema, ObjectEditSchema, ObjectResponseSchema
from services.objects import ObjectsService


router = APIRouter(prefix="/objects", tags=["Objects"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await ObjectsService().get_all(uow=uow)
    return res


@router.get(path="_with_company")
async def get_all_with_company(uow: UOWDep):
    res = await ObjectsService().get_all_with_company(uow=uow)
    return res


@router.get(path="_by_company_id/{id}")
async def get_all_by_company_id(id: int, uow: UOWDep):
    res = await ObjectsService().get_all_by_company_id(uow=uow, params=dict(company_id=id))
    return res


@router.get(path="/{id}")
async def get_one(id: int, uow: UOWDep):
    res = await ObjectsService().get_one(uow=uow, params=dict(id=id))
    return res


@router.get(path="_with_company/{id}")
async def get_one_with_company(id: int, uow: UOWDep):
    res = await ObjectsService().get_one_with_company(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: ObjectAddSchema, uow: UOWDep):
    id = await ObjectsService().add(uow=uow, schema=schema)
    return {"object_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: ObjectEditSchema, uow: UOWDep):
    await ObjectsService().edit(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await ObjectsService().delete(uow=uow, params=dict(id=id))
    return {"ok": True}