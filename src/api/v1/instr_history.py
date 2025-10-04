from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.instr_history import InstrHistoryAddSchema
from services.instr_history import InstrHistoryService


router = APIRouter(prefix="/instr_history", tags=["InstrHistory"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await InstrHistoryService().get_all(uow=uow)
    return res


@router.get(path="_with_other")
async def get_all_with_other(uow: UOWDep):
    res = await InstrHistoryService().get_all_with_other(uow=uow)
    return res


@router.get(path="/{id}")
async def get_one(id: int, uow: UOWDep):
    res = await InstrHistoryService().get_one(uow=uow, params=dict(id=id))
    return res


@router.get(path="_with_other/{id}")
async def get_one_with_other(id: int, uow: UOWDep):
    res = await InstrHistoryService().get_one_with_other(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: InstrHistoryAddSchema, uow: UOWDep):
    id = await InstrHistoryService().add(uow=uow, schema=schema)
    return {"instr_hist_id": id}