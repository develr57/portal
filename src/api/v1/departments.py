import uuid
from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.departments import DepartmentAddSchema, DepartmentEditSchema
from services.departments import DepartmentsService


router = APIRouter(prefix="/departments", tags=["Departments"])


@router.get(path="")
async def get_all(uow: UOWDep):
    departments = await DepartmentsService().get_departments(uow)
    return departments


@router.get(path="/{id}")
async def get_one(id: uuid.UUID, uow: UOWDep):
    department = await DepartmentsService().get_department(uow, dict(id=id))
    return department


@router.post("")
async def add(schema: DepartmentAddSchema, uow: UOWDep):
    id = await DepartmentsService().add_department(uow, schema)
    return {"company_id": id}


@router.patch("/{id}")
async def edit(id: uuid.UUID, schema: DepartmentEditSchema, uow: UOWDep):
    await DepartmentsService().edit_department(uow, id, schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: uuid.UUID, uow: UOWDep):
    await DepartmentsService().delete_department(uow=uow, id=id)
    return {"ok": True}