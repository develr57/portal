from _datetime import datetime
from pydantic import BaseModel


class StorageAddSchema(BaseModel):
    storage: str
    description: str
    dept_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class StorageEditSchema(BaseModel):
    storage: str
    description: str
    dept_id: int
    updated_at: datetime


class StorageResponseSchema(StorageAddSchema):
    id: int


class StorageResponseSchemaWithDepartment(StorageResponseSchema):
    dept_name: str
    dept_full_name: str
