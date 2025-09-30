from _datetime import datetime
from pydantic import BaseModel


class StatusAddSchema(BaseModel):
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class StatusEditSchema(BaseModel):
    status: str
    updated_at: datetime


class StatusResponseSchema(StatusAddSchema):
    id: int
