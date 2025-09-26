from typing import TYPE_CHECKING
from models.base import Base, uuid_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from schemas.departments import DepartmentResponseSchema

if TYPE_CHECKING:
    from src.models.companies import Companies


class Departments(Base):
    __tablename__ = "departments"

    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(String(100))
    full_name: Mapped[str] = mapped_column(String(150))
    company_id: Mapped[uuid_pk] = mapped_column(ForeignKey("companies.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    company: Mapped["Companies"] = relationship(back_populates="departments")

    def to_read_model(self) -> "DepartmentResponseSchema":
        return DepartmentResponseSchema(
            id=self.id,
            name=self.name,
            full_name=self.full_name,
            company_id=self.company_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
