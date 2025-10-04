from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.employees import EmployeeAddSchema, EmployeeEditSchema
from services.employees import EmployeesService


router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get(path="")
async def get_all(uow: UOWDep):
    res = await EmployeesService().get_all(uow=uow)
    return res


@router.get(path="_with_other")
async def get_all_with_other(uow: UOWDep):
    res = await EmployeesService().get_all_with_other(uow=uow)
    return res


@router.get(path="/{id}")
async def get_one(id: int, uow: UOWDep):
    res = await EmployeesService().get_one(uow=uow, params=dict(id=id))
    return res


@router.get(path="_with_other/{id}")
async def get_one_with_other(id: int, uow: UOWDep):
    res = await EmployeesService().get_one_with_other(uow=uow, params=dict(id=id))
    return res


@router.post("")
async def add(schema: EmployeeAddSchema, uow: UOWDep):
    id = await EmployeesService().add(uow=uow, schema=schema)
    return {"emp_id": id}


@router.patch("/{id}")
async def edit(id: int, schema: EmployeeEditSchema, uow: UOWDep):
    await EmployeesService().edit(uow=uow, params=dict(id=id), schema=schema)
    return {"ok": True}


@router.delete("/{id}")
async def delete(id: int, uow: UOWDep):
    await EmployeesService().delete(uow=uow, params=dict(id=id))
    return {"ok": True}