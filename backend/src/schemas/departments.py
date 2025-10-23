from _datetime import datetime
from pydantic import BaseModel


class DepartmentAddSchema(BaseModel):
    name: str
    full_name: str
    company_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class DepartmentEditSchema(BaseModel):
    name: str
    full_name: str
    company_id: int
    updated_at: datetime


class DepartmentResponseSchema(DepartmentAddSchema):
    id: int


class DepartmentResponseSchemaWithCompany(DepartmentResponseSchema):
    company_name: str
    company_full_name: str
