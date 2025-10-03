from typing import TYPE_CHECKING
from models.base import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from schemas.departments import DepartmentResponseSchema, DepartmentResponseSchemaWithCompany

if TYPE_CHECKING:
    from companies import Companies
    from instruments import Instruments


class Departments(Base):
    __tablename__ = "departments"

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    full_name: Mapped[str] = mapped_column(String(150), nullable=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id", ondelete="RESTRICT"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    company: Mapped["Companies"] = relationship(back_populates="departments")
    instruments: Mapped[list["Instruments"]] = relationship(back_populates="department")

    def to_read_model(self) -> "DepartmentResponseSchema":
        return DepartmentResponseSchema(
            id=self.id,
            name=self.name,
            full_name=self.full_name,
            company_id=self.company_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


    def to_read_model_with_company(self) -> "DepartmentResponseSchemaWithCompany":
        return DepartmentResponseSchemaWithCompany(
            id=self.id,
            name=self.name,
            full_name=self.full_name,
            company_id=self.company_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            company_name=self.company.name,
            company_full_name=self.company.full_name
        )
