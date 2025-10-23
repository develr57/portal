from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.departments import DepartmentAddSchema, DepartmentEditSchema
from services.departments import DepartmentsService


router = APIRouter(prefix="/departments", tags=["Departments"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await DepartmentsService().get_all(uow=uow)
    return res


@router.get(path="_with_company")
async def get_all_with_company(uow: UOWDep):
    res = await DepartmentsService().get_all_with_company(uow=uow)
    return res


@router.get(path="/{id}")
async def get_one(id: int, uow: UOWDep):
    res = await DepartmentsService().get_one(uow=uow, params=dict(id=id))
    return res


@router.get(path="_with_company/{id}")
async def get_one_with_company(id: int, uow: UOWDep):
    res = await DepartmentsService().get_one_with_company(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: DepartmentAddSchema, uow: UOWDep):
    id = await DepartmentsService().add(uow=uow, schema=schema)
    return {"dept_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: DepartmentEditSchema, uow: UOWDep):
    await DepartmentsService().edit(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await DepartmentsService().delete(uow=uow, params=dict(id=id))
    return {"ok": True}