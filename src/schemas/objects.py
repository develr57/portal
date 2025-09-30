import uuid
from _datetime import datetime
from pydantic import BaseModel


class ObjectAddSchema(BaseModel):
    name: str
    full_name: str
    company_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ObjectEditSchema(BaseModel):
    name: str
    full_name: str
    company_id: int
    updated_at: datetime


class ObjectResponseSchema(ObjectAddSchema):
    id: int


class ObjectResponseSchemaWithCompany(ObjectResponseSchema):
    company_name: str
    company_full_name: str
