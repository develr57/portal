from _datetime import datetime
from pydantic import BaseModel


class EmployeeEditSchema(BaseModel):
    name: str
    full_name: str
    company_id: int
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
