import datetime
from pydantic import BaseModel
from sqlalchemy import BigInteger


class CompanySchema(BaseModel):
    id: BigInteger
    name: str
    full_name: str
    created_at: datetime.datetime.now(datetime.UTC)
    updated_at: datetime.datetime.now(datetime.UTC)

    class Config:
        from_attributes = True


class CompanySchemaAdd(BaseModel):
    name: str
    full_name: str


class CompanySchemaEdit(BaseModel):
    name: str
    full_name: str
    updated_at: datetime.datetime.now(datetime.UTC)
