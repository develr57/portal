import uuid
from _datetime import datetime
from pydantic import BaseModel


class DepartmentAddSchema(BaseModel):
    name: str
    full_name: str
    company_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class DepartmentEditSchema(BaseModel):
    name: str
    full_name: str
    company_id: uuid.UUID
    updated_at: datetime


class DepartmentResponseSchema(DepartmentAddSchema):
    id: uuid.UUID


class DepartmentResponseSchemaWithCompany(DepartmentResponseSchema):
    company_name: str
    company_full_name: str
