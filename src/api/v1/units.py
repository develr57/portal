from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.units import UnitAddSchema, UnitEditSchema, UnitResponseSchema
from services.units import UnitsService


router = APIRouter(prefix="/units", tags=["Units"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await UnitsService().get_all(uow=uow)
    return res


@router.get(path="/{id}", response_model=UnitResponseSchema)
async def get_one(id: int, uow: UOWDep):
    res = await UnitsService().get_one(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: UnitAddSchema, uow: UOWDep):
    id = await UnitsService().add(uow=uow, schema=schema)
    return {"unit_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: UnitEditSchema, uow: UOWDep):
    await UnitsService().edit(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await UnitsService().delete(uow=uow, params=dict(id=id))
    return {"ok": True}