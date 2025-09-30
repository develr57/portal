from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.storages import StorageAddSchema, StorageEditSchema
from services.storages import StoragesService


router = APIRouter(prefix="/storages", tags=["Storages"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await StoragesService().get_storages(uow=uow)
    return res


@router.get(path="_with_dept")
async def get_all_with_company(uow: UOWDep):
    res = await StoragesService().get_storages_with_dept(uow=uow)
    return res


@router.get(path="/{id}")
async def get_one(id: int, uow: UOWDep):
    res = await StoragesService().get_storage(uow=uow, params=dict(id=id))
    return res


@router.get(path="_with_dept/{id}")
async def get_one(id: int, uow: UOWDep):
    res = await StoragesService().get_storage_with_dept(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: StorageAddSchema, uow: UOWDep):
    id = await StoragesService().add_storage(uow=uow, schema=schema)
    return {"storage_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: StorageEditSchema, uow: UOWDep):
    await StoragesService().edit_storage(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await StoragesService().delete_storage(uow=uow, params=dict(id=id))
    return {"ok": True}