from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.ints_points import InstPointAddSchema, InstPointEditSchema
from services.inst_points import InstPointsService


router = APIRouter(prefix="/inst_points", tags=["InstPoints"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await InstPointsService().get_all(uow=uow)
    return res


@router.get(path="_with_dept")
async def get_all_with_company(uow: UOWDep):
    res = await InstPointsService().get_all_with_dept(uow=uow)
    return res


@router.get(path="/{id}")
async def get_one(id: int, uow: UOWDep):
    res = await InstPointsService().get_one(uow=uow, params=dict(id=id))
    return res


@router.get(path="_with_dept/{id}")
async def get_one(id: int, uow: UOWDep):
    res = await InstPointsService().get_one_with_dept(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: InstPointAddSchema, uow: UOWDep):
    id = await InstPointsService().add(uow=uow, schema=schema)
    return {"inst_point_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: InstPointEditSchema, uow: UOWDep):
    await InstPointsService().edit(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await InstPointsService().delete(uow=uow, params=dict(id=id))
    return {"ok": True}