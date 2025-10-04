from typing import TYPE_CHECKING
from models.base import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Float, Date, SmallInteger
from schemas.instr_history import InstrHistoryResponseSchema, InstrHistoryResponseSchemaWithOthers
import datetime

if TYPE_CHECKING:
    from companies import Companies
    from departments import Departments
    from employees import Employees
    from inst_points import InstPoints
    from instr_types import InstrTypes
    from instruments import Instruments
    from manufacturers import Manufacturers
    from objects import Objects
    from statuses import Statuses
    from storages import Storages
    from units import Units


class InstrHistory(Base):
    __tablename__ = "instr_history"

    id: Mapped[int_pk]
    instr_id: Mapped[int] = mapped_column(ForeignKey("instruments.id", ondelete="RESTRICT"))
    manuf_id: Mapped[int] = mapped_column(ForeignKey("manufacturers.id", ondelete="RESTRICT"))
    instr_type_id: Mapped[int] = mapped_column(ForeignKey("instr_types.id", ondelete="RESTRICT"))
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    inv_num: Mapped[str] = mapped_column(String(20), nullable=False)
    serial_num: Mapped[str] = mapped_column(String(50), nullable=False)
    label_num: Mapped[int] = mapped_column(String(20), nullable=False)
    range: Mapped[str] = mapped_column(String(20), nullable=False)
    unit_id: Mapped[int] = mapped_column(ForeignKey("units.id", ondelete="RESTRICT"))
    val_scale_div: Mapped[float] = mapped_column(Float(), nullable=False, default=0.0)
    accuracy_class: Mapped[float] = mapped_column(Float(), nullable=False, default=0.0)
    commiss_date: Mapped[datetime.date] = mapped_column(Date)
    last_verify_date: Mapped[datetime.date] = mapped_column(Date)
    next_verify_date: Mapped[datetime.date] = mapped_column(Date)
    verif_interval: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    status_id: Mapped[int] = mapped_column(ForeignKey("statuses.id", ondelete="RESTRICT"))
    inst_object_id: Mapped[int] = mapped_column(ForeignKey("objects.id", ondelete="RESTRICT"))
    inst_point_id: Mapped[int] = mapped_column(ForeignKey("inst_points.id", ondelete="RESTRICT"))
    stor_object_id: Mapped[int] = mapped_column(ForeignKey("objects.id", ondelete="RESTRICT"))
    storage_id: Mapped[int] = mapped_column(ForeignKey("storage.id", ondelete="RESTRICT"))
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id", ondelete="RESTRICT"))
    dept_id: Mapped[int] = mapped_column(ForeignKey("departments.id", ondelete="RESTRICT"))
    emp_id: Mapped[int] = mapped_column(ForeignKey("employees.id", ondelete="RESTRICT"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    company: Mapped["Companies"] = relationship(back_populates="instr_history")
    department: Mapped["Departments"] = relationship(back_populates="instr_history")
    employee: Mapped["Employees"] = relationship(back_populates="instr_history")
    inst_point: Mapped["InstPoints"] = relationship(back_populates="instr_history")
    instr_type: Mapped["InstrTypes"] = relationship(back_populates="instr_history")
    instrument: Mapped["Instruments"] = relationship(back_populates="instr_history")
    manufacturer: Mapped["Manufacturers"] = relationship(back_populates="instr_history")
    object: Mapped["Objects"] = relationship(back_populates="instr_history")
    status: Mapped["Statuses"] = relationship(back_populates="instr_history")
    storage: Mapped["Storages"] = relationship(back_populates="instr_history")
    unit: Mapped["Units"] = relationship(back_populates="instr_history")


    def to_read_model(self) -> "InstrHistoryResponseSchema":
        return InstrHistoryResponseSchema(
            id=self.id,
            instr_id=self.instr_id,
            manuf_id=self.manuf_id,
            instr_type_id=self.instr_type_id,
            model=self.model,
            inv_num=self.inv_num,
            serial_num=self.serial_num,
            label_num=self.label_num,
            range=self.range,
            unit_id=self.unit_id,
            val_scale_div=self.val_scale_div,
            accuracy_class=self.accuracy_class,
            commiss_date=self.commiss_date,
            last_verify_date=self.last_verify_date,
            next_verify_date=self.next_verify_date,
            verif_interval=self.verif_interval,
            status_id=self.status_id,
            inst_object_id=self.inst_object_id,
            inst_point_id=self.inst_point_id,
            stor_object_id=self.stor_object_id,
            storage_id=self.storage_id,
            company_id=self.company_id,
            dept_id=self.dept_id,
            emp_id=self.emp_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


    def to_read_model_with_all(self) -> "InstrHistoryResponseSchemaWithOthers":
        return InstrHistoryResponseSchemaWithOthers(
            id=self.id,
            instr_id=self.instr_id,
            manuf_id=self.manuf_id,
            instr_type_id=self.instr_type_id,
            model=self.model,
            inv_num=self.inv_num,
            serial_num=self.serial_num,
            label_num=self.label_num,
            range=self.range,
            unit_id=self.unit_id,
            val_scale_div=self.val_scale_div,
            accuracy_class=self.accuracy_class,
            commiss_date=self.commiss_date,
            last_verify_date=self.last_verify_date,
            next_verify_date=self.next_verify_date,
            verif_interval=self.verif_interval,
            status_id=self.status_id,
            inst_object_id=self.inst_object_id,
            inst_point_id=self.inst_point_id,
            stor_object_id=self.stor_object_id,
            storage_id=self.storage_id,
            company_id=self.company_id,
            dept_id=self.dept_id,
            emp_id=self.emp_id,
            created_at=self.created_at,
            updated_at=self.updated_at,

            manuf_name=self.manufacturer.name,
            manuf_full_name=self.manufacturer.full_name,
            instr_type_name=self.instr_type.name,
            instr_full_name=self.instr_type.full_name,
            unit=self.unit.unit,
            status=self.status.status,
            inst_object_name=self.object.name,
            inst_object_full_name=self.object.full_name,
            inst_point=self.inst_point.point,
            inst_point_descr=self.inst_point.description,
            stor_object_name=self.object.name,
            stor_object_full_name=self.object.full_name,
            storage=self.storage.storage,
            storage_descr=self.storage.description,
            company_name=self.company.name,
            company_full_name=self.company.full_name,
            dept_name=self.department.name,
            dept_full_name=self.department.full_name,
            emp_surname=self.employee.surname,
            emp_name=self.employee.name,
            emp_patronymic=self.employee.patronymic,
            emp_position=self.employee.position,
        )
