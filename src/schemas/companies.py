from _datetime import datetime
from pydantic import BaseModel, ConfigDict


class CompanySchemaBase(BaseModel):
    id: int
    name: str
    full_name: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CompanySchemaAdd(CompanySchemaBase):
    name: str
    full_name: str


class CompanySchemaEdit(CompanySchemaBase):
    name: str
    full_name: str
    updated_at: datetime
