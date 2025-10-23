from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.instr_types import InstrTypeAddSchema, InstrTypeEditSchema, InstrTypeResponseSchema
from services.instr_types import InstrTypesService


router = APIRouter(prefix="/types", tags=["Types"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await InstrTypesService().get_all(uow=uow)
    return res


@router.get(path="/{id}", response_model=InstrTypeResponseSchema)
async def get_one(id: int, uow: UOWDep):
    res = await InstrTypesService().get_one(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: InstrTypeAddSchema, uow: UOWDep):
    id = await InstrTypesService().add(uow=uow, schema=schema)
    return {"instr_type_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: InstrTypeEditSchema, uow: UOWDep):
    await InstrTypesService().edit(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await InstrTypesService().delete(uow=uow, params=dict(id=id))
    return {"ok": True}