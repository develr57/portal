from typing import TYPE_CHECKING
from models.base import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Boolean
from schemas.employees import EmployeeResponseSchema, EmployeeResponseSchemaWithOthers

if TYPE_CHECKING:
    from companies import Companies
    from departments import Departments
    from instr_history import InstrHistory
    from users import Users


class Employees(Base):
    __tablename__ = "employees"

    id: Mapped[int_pk]
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    patronymic: Mapped[str] = mapped_column(String(50), nullable=False)
    position: Mapped[str] = mapped_column(String(100), nullable=False)
    is_dept_head: Mapped[bool] = mapped_column(Boolean, default=False)
    is_dept_deputy_head: Mapped[bool] = mapped_column(Boolean, default=False)
    is_metrologist: Mapped[bool] = mapped_column(Boolean, default=False)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id", ondelete="RESTRICT"))
    dept_id: Mapped[int] = mapped_column(ForeignKey("departments.id", ondelete="RESTRICT"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    company: Mapped["Companies"] = relationship(back_populates="employees")
    department: Mapped["Departments"] = relationship(back_populates="employees")
    instr_history: Mapped[list["InstrHistory"]] = relationship(back_populates="employee")
    user: Mapped["Users"] = relationship(back_populates="employee", uselist=False)

    def to_read_model(self) -> "EmployeeResponseSchema":
        return EmployeeResponseSchema(
            id=self.id,
            surname=self.surname,
            name=self.name,
            patronymic=self.patronymic,
            position=self.position,
            is_dept_head=self.is_dept_head,
            is_dept_deputy_head=self.is_dept_deputy_head,
            is_metrologist=self.is_metrologist,
            company_id=self.company_id,
            dept_id=self.dept_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


    def to_read_model_with_all(self) -> "EmployeeResponseSchemaWithOthers":
        return EmployeeResponseSchemaWithOthers(
            id=self.id,
            surname=self.surname,
            name=self.name,
            patronymic=self.patronymic,
            position=self.position,
            is_dept_head=self.is_dept_head,
            is_dept_deputy_head=self.is_dept_deputy_head,
            is_metrologist=self.is_metrologist,
            company_id=self.company_id,
            dept_id=self.dept_id,
            created_at=self.created_at,
            updated_at=self.updated_at,

            company_name=self.company.name,
            company_full_name=self.company.full_name,
            dept_name=self.department.name,
            dept_full_name=self.department.full_name,
        )
