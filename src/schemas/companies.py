import uuid
from _datetime import datetime
from pydantic import BaseModel


class CompanyAddSchema(BaseModel):
    # id: uuid.UUID
    name: str
    full_name: str
    created_at: datetime
    updated_at: datetime


class CompanyEditSchema(BaseModel):
    name: str
    full_name: str
    updated_at: datetime


class CompanyResponseSchema(BaseModel):
    id: uuid.UUID
    name: str
    full_name: str
    created_at: datetime
    updated_at: datetime
