import datetime
from pydantic import BaseModel
from sqlalchemy import BigInteger


class DepartmentsSchema(BaseModel):
    id: BigInteger
    name: str
    full_name: str
    company_id: BigInteger
    created_at: datetime.datetime.now(datetime.UTC)
    updated_at: datetime.datetime.now(datetime.UTC)

    class Config:
        from_attributes = True


class DepartmentEditSchema(BaseModel):
    updated_at: datetime.datetime.now(datetime.UTC)