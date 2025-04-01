import datetime
from pydantic import BaseModel
from sqlalchemy import BigInteger


class CompaniesSchema(BaseModel):
    id: BigInteger
    name: str
    full_name: str
    created_at: datetime.datetime.now(datetime.UTC)
    updated_at: datetime.datetime.now(datetime.UTC)

    class Config:
        from_attributes = True


class CompaniesEditSchema(BaseModel):
    updated_at: datetime.datetime.now(datetime.UTC)
