import datetime
from pydantic import BaseModel, ConfigDict


class DepartmentSchema(BaseModel):
    id: int
    name: str
    full_name: str
    company_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DepartmentSchemaAdd(BaseModel):
    name: str
    full_name: str
    company_id: int


class DepartmentSchemaEdit(BaseModel):
    updated_at: datetime