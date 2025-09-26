import uuid
from _datetime import datetime
from pydantic import BaseModel


class DepartmentAddSchema(BaseModel):
    # id: uuid.UUID
    name: str
    full_name: str
    company_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class DepartmentEditSchema(BaseModel):
    name: str
    full_name: str
    company_id: uuid.UUID
    updated_at: datetime


class DepartmentResponseSchema(BaseModel):
    id: uuid.UUID
    name: str
    full_name: str
    company_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
