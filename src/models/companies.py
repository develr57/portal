from typing import TYPE_CHECKING
from models.base import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from schemas.companies import CompanyResponseSchema

if TYPE_CHECKING:
    from departments import Departments
    from instruments import Instruments
    from objects import Objects


class Companies(Base):
    __tablename__ = "companies"

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    full_name: Mapped[str] = mapped_column(String(150), nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    departments: Mapped[list["Departments"]] = relationship(back_populates="company")
    instruments: Mapped[list["Instruments"]] = relationship(back_populates="company")
    objects: Mapped[list["Objects"]] = relationship(back_populates="company")

    def to_read_model(self) -> "CompanyResponseSchema":
        return CompanyResponseSchema(
            id=self.id,
            name=self.name,
            full_name=self.full_name,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
