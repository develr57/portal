from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.manufacturers import ManufacturerAddSchema, ManufacturerEditSchema, ManufacturerResponseSchema
from services.manufacturers import ManufacturersService


router = APIRouter(prefix="/manufacturers", tags=["Manufacturers"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await ManufacturersService().get_all(uow=uow)
    return res


@router.get(path="/{id}", response_model=ManufacturerResponseSchema)
async def get_one(id: int, uow: UOWDep):
    res = await ManufacturersService().get_one(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: ManufacturerAddSchema, uow: UOWDep):
    id = await ManufacturersService().add(uow=uow, schema=schema)
    return {"manufacturer_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: ManufacturerEditSchema, uow: UOWDep):
    await ManufacturersService().edit(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await ManufacturersService().delete(uow=uow, params=dict(id=id))
    return {"ok": True}