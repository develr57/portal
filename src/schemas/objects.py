import uuid
from _datetime import datetime
from pydantic import BaseModel


class ObjectAddSchema(BaseModel):
    name: str
    full_name: str
    company_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class ObjectEditSchema(BaseModel):
    name: str
    full_name: str
    company_id: uuid.UUID
    updated_at: datetime


class ObjectResponseSchema(ObjectAddSchema):
    id: int

    class Config:
        from_attributes = True


class ObjectResponseSchemaWithCompany(ObjectResponseSchema):
    company_name: str
    company_full_name: str
