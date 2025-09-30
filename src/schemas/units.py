from _datetime import datetime
from pydantic import BaseModel


class UnitAddSchema(BaseModel):
    unit: str
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UnitEditSchema(BaseModel):
    unit: str
    description: str
    updated_at: datetime


class UnitResponseSchema(UnitAddSchema):
    id: int
