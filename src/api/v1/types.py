from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.types import TypeAddSchema, TypeEditSchema, TypeResponseSchema
from services.types import TypesService


router = APIRouter(prefix="/types", tags=["Types"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await TypesService().get_all(uow=uow)
    return res


@router.get(path="/{id}", response_model=TypeResponseSchema)
async def get_one(id: int, uow: UOWDep):
    res = await TypesService().get_one(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: TypeAddSchema, uow: UOWDep):
    id = await TypesService().add(uow=uow, schema=schema)
    return {"type_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: TypeEditSchema, uow: UOWDep):
    await TypesService().edit(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await TypesService().delete(uow=uow, params=dict(id=id))
    return {"ok": True}