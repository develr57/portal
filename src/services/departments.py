import uuid
from utils.unitofwork import IUnitOfWork
from schemas.departments import DepartmentAddSchema, DepartmentEditSchema


class DepartmentsService:

    async def get_departments(self, uow: IUnitOfWork):
        async with uow:
            departments = await uow.departments.find_all()
            return departments


    async def get_department(self, uow: IUnitOfWork, data: dict):
        async with uow:
            department = await uow.departments.find_one(data)
            return department


    async def add_department(self, uow: IUnitOfWork, schema: DepartmentAddSchema) -> uuid.UUID:
        departments_dict = schema.model_dump()
        async with uow:
            id = await uow.departments.add_one(departments_dict)
            await uow.commit()
            return id


    async def edit_department(self, uow: IUnitOfWork, id: uuid.UUID, schema: DepartmentEditSchema):
        departments_dict = schema.model_dump()
        async with uow:
            await uow.departments.edit_one(id, departments_dict)
            await uow.commit()


    async def delete_department(self, uow: IUnitOfWork, id: uuid.UUID):
        async with uow:
            await uow.departments.delete(id)
            await uow.commit()
