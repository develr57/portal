import uuid
from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.departments import DepartmentAddSchema, DepartmentEditSchema
from services.departments import DepartmentsService


router = APIRouter(prefix="/departments", tags=["Departments"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await DepartmentsService().get_departments(uow=uow)
    return res


@router.get(path="_with_company")
async def get_all_with_company(uow: UOWDep):
    res = await DepartmentsService().get_departments_with_company(uow=uow)
    return res


@router.get(path="/{id}")
async def get_one(id: uuid.UUID, uow: UOWDep):
    res = await DepartmentsService().get_department(uow=uow, params=dict(id=id))
    return res


@router.get(path="_with_company/{id}")
async def get_one(id: uuid.UUID, uow: UOWDep):
    res = await DepartmentsService().get_department_with_company(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: DepartmentAddSchema, uow: UOWDep):
    id = await DepartmentsService().add_department(uow=uow, schema=schema)
    return {"dept_id": id}


@router.patch("/{id}")
async def edit(id: uuid.UUID, schema: DepartmentEditSchema, uow: UOWDep):
    await DepartmentsService().edit_department(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: uuid.UUID, uow: UOWDep):
    await DepartmentsService().delete_department(uow=uow, params=dict(id=id))
    return {"ok": True}