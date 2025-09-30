from _datetime import datetime
from pydantic import BaseModel


class TypeAddSchema(BaseModel):
    name: str
    full_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TypeEditSchema(BaseModel):
    name: str
    full_name: str
    updated_at: datetime


class TypeResponseSchema(TypeAddSchema):
    id: int
