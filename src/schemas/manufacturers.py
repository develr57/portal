import uuid
from _datetime import datetime
from pydantic import BaseModel


class ManufacturerAddSchema(BaseModel):
    name: str
    full_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ManufacturerEditSchema(BaseModel):
    name: str
    full_name: str
    updated_at: datetime


class ManufacturerResponseSchema(ManufacturerAddSchema):
    id: int

