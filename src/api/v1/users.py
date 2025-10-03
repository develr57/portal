from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.users import UserAddSchema, UserEditSchema
from services.users import UsersService


router = APIRouter(prefix="/users", tags=["Users"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await UsersService().get_all(uow=uow)
    return res


@router.get(path="_with_emp")
async def get_all_with_emp(uow: UOWDep):
    res = await UsersService().get_all_with_emp(uow=uow)
    return res


@router.get(path="/{id}")
async def get_one(id: int, uow: UOWDep):
    res = await UsersService().get_one(uow=uow, params=dict(id=id))
    return res


@router.get(path="_with_emp/{id}")
async def get_one(id: int, uow: UOWDep):
    res = await UsersService().get_one_with_emp(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: UserAddSchema, uow: UOWDep):
    id = await UsersService().add(uow=uow, schema=schema)
    return {"user_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: UserEditSchema, uow: UOWDep):
    await UsersService().edit(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await UsersService().delete(uow=uow, params=dict(id=id))
    return {"ok": True}