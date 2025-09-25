import uuid
from _datetime import datetime
from pydantic import BaseModel, ConfigDict


class CompanyCreateSchema(BaseModel):
    # id: uuid.UUID
    name: str
    full_name: str
    created_at: datetime
    updated_at: datetime

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [{
    #             "name": "ТОО АМК",
    #             "full_name": "Товарищество с ограниченной ответственностью Актюбинская медная компания",
    #         }]
    #     }
    # }


class CompanyUpdateSchema(BaseModel):
    name: str
    full_name: str
    updated_at: datetime


class CompanyResponseSchema(BaseModel):
    id: uuid.UUID
    name: str
    full_name: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "name": "ТОО АМК",
                "full_name": "Товарищество с ограниченной ответственностью Актюбинская медная компания",
            }]
        }
    }