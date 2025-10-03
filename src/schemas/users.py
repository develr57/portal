from _datetime import datetime
from pydantic import BaseModel


class UserEditSchema(BaseModel):
    username: str
    email: str
    is_admin: bool
    is_disabled: bool
    emp_id: int
    updated_at: datetime

    class Config:
        from_attributes = True


class UserChangePasswordSchema(BaseModel):
    password_hash: str
    updated_at: datetime


class UserAddSchema(UserEditSchema):
    password_hash: str
    created_at: datetime


class UserResponseSchema(UserAddSchema):
    id: int


class UserResponseSchemaWithEmp(UserResponseSchema):
    surname: str
    name: str
    patronymic: str
    position: str
    is_dept_head: bool
    is_dept_deputy_head: bool
    is_metrologist: bool
    company_id: int
    dept_id: int
