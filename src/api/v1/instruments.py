from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.instruments import InstrumentAddSchema, InstrumentEditSchema
from services.instruments import InstrumentsService


router = APIRouter(prefix="/instruments", tags=["Instruments"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await InstrumentsService().get_all(uow=uow)
    return res


@router.get(path="_with_other")
async def get_all_with_other(uow: UOWDep):
    res = await InstrumentsService().get_all_with_other(uow=uow)
    return res


@router.get(path="/{id}")
async def get_one(id: int, uow: UOWDep):
    res = await InstrumentsService().get_one(uow=uow, params=dict(id=id))
    return res


@router.get(path="_with_other/{id}")
async def get_one_with_other(id: int, uow: UOWDep):
    res = await InstrumentsService().get_one_with_other(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: InstrumentAddSchema, uow: UOWDep):
    id = await InstrumentsService().add(uow=uow, schema=schema)
    return {"instr_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: InstrumentEditSchema, uow: UOWDep):
    await InstrumentsService().edit(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await InstrumentsService().delete(uow=uow, params=dict(id=id))
    return {"ok": True}