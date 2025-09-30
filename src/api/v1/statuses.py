from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.statuses import StatusAddSchema, StatusEditSchema, StatusResponseSchema
from services.statuses import StatusesService


router = APIRouter(prefix="/statuses", tags=["Statuses"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await StatusesService().get_statuses(uow=uow)
    return res


@router.get(path="/{id}", response_model=StatusResponseSchema)
async def get_one(id: int, uow: UOWDep):
    res = await StatusesService().get_status(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: StatusAddSchema, uow: UOWDep):
    id = await StatusesService().add_status(uow=uow, schema=schema)
    return {"status_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: StatusEditSchema, uow: UOWDep):
    await StatusesService().edit_status(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await StatusesService().delete_status(uow=uow, params=dict(id=id))
    return {"ok": True}