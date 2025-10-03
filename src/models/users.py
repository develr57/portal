from typing import TYPE_CHECKING
from models.base import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Boolean
from schemas.users import UserResponseSchema, UserResponseSchemaWithEmp

if TYPE_CHECKING:
    from employees import Employees


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int_pk]
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(256), nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_disabled: Mapped[bool] = mapped_column(Boolean, default=False)
    emp_id: Mapped[int] = mapped_column(ForeignKey("employees.id", ondelete="RESTRICT"), nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    employee: Mapped["Employees"] = relationship(back_populates="user")

    def to_read_model(self) -> "UserResponseSchema":
        return UserResponseSchema(
            id=self.id,
            username=self.username,
            email=self.email,
            is_admin=self.is_admin,
            is_disabled=self.is_disabled,
            emp_id=self.emp_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


    def to_read_model_with_emp(self) -> "UserResponseSchemaWithEmp":
        return UserResponseSchemaWithEmp(
            id=self.id,
            username=self.username,
            email=self.email,
            is_admin=self.is_admin,
            is_disabled=self.is_disabled,
            emp_id=self.emp_id,
            created_at=self.created_at,
            updated_at=self.updated_at,

            surname=self.employee.surname,
            name=self.employee.name,
            patronymic=self.employee.patronymic,
            position=self.employee.position,
            is_dept_head=self.employee.is_dept_head,
            is_dept_deputy_head=self.employee.is_dept_deputy_head,
            is_metrologist=self.employee.is_metrologist,
            company_id=self.employee.company_id,
            dept_id=self.employee.dept_id,
        )
