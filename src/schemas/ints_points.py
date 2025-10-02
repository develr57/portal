from _datetime import datetime
from pydantic import BaseModel


class InstPointAddSchema(BaseModel):
    point: str
    description: str
    dept_id: int
    object_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class InstPointEditSchema(BaseModel):
    point: str
    description: str
    dept_id: int
    object_id: int
    updated_at: datetime


class InstPointResponseSchema(InstPointAddSchema):
    id: int


class InstPointResponseSchemaWithDeptAndObject(InstPointResponseSchema):
    dept_name: str
    dept_full_name: str
    object_name: str
    object_full_name: str
