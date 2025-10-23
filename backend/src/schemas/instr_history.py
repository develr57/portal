from _datetime import datetime
from datetime import date
from pydantic import BaseModel


class InstrHistoryAddSchema(BaseModel):
    instr_id: int
    manuf_id: int
    instr_type_id: int
    model: str
    inv_num: str
    serial_num: str
    label_num: str
    range: str
    unit_id: int
    val_scale_div: float
    accuracy_class: float
    commiss_date: date
    last_verify_date: date
    next_verify_date: date
    verif_interval: int
    status_id: int
    inst_object_id: int
    inst_point_id: int
    stor_object_id: int
    storage_id: int
    company_id: int
    dept_id: int
    emp_id:int
    created_at: datetime

    class Config:
        from_attributes = True
    


class InstrHistoryResponseSchema(InstrHistoryAddSchema):
    id: int


class InstrHistoryResponseSchemaWithOthers(InstrHistoryResponseSchema):
    manuf_name: str
    manuf_full_name: str
    instr_type_name: str
    instr_full_name: str
    unit: str
    status: str
    inst_object_name: str
    inst_object_full_name: str
    inst_point: str
    inst_point_descr: str
    stor_object_name: str
    stor_object_full_name: str
    storage: str
    storage_descr: str
    company_name: str
    company_full_name: str
    dept_name: str
    dept_full_name: str
    emp_surname: str
    emp_name: str
    emp_patronymic: str
    emp_position: str
