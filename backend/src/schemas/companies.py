from _datetime import datetime
from pydantic import BaseModel


class CompanyAddSchema(BaseModel):
    name: str
    full_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CompanyEditSchema(BaseModel):
    name: str
    full_name: str
    updated_at: datetime


class CompanyResponseSchema(CompanyAddSchema):
    id: int
