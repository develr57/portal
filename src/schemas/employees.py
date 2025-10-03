from _datetime import datetime
from pydantic import BaseModel


class EmployeeEditSchema(BaseModel):
    surname: str
    name: str
    patronymic: str
    position: str
    is_dept_head: bool
    is_dept_deputy_head: bool
    is_metrologist: bool
    company_id: int
    dept_id: int
    updated_at: datetime

    class Config:
        from_attributes = True


class EmployeeAddSchema(EmployeeEditSchema):
    created_at: datetime


class EmployeeResponseSchema(EmployeeAddSchema):
    id: int


class EmployeeResponseSchemaWithOthers(EmployeeResponseSchema):
    company_name: str
    company_full_name: str
    dept_name: str
    dept_full_name: str
