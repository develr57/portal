import datetime
from pydantic import BaseModel
from sqlalchemy import BigInteger


class DepartmentSchema(BaseModel):
    id: BigInteger
    name: str
    full_name: str
    company_id: BigInteger
    created_at: datetime.datetime.now(datetime.UTC)
    updated_at: datetime.datetime.now(datetime.UTC)

    class Config:
        from_attributes = True


class DepartmentScemaAdd(BaseModel):
    name: str
    full_name: str
    company_id: BigInteger


class DepartmentSchemaEdit(BaseModel):
    updated_at: datetime.datetime.now(datetime.UTC)