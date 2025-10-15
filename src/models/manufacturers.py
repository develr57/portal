from typing import TYPE_CHECKING
from models.base import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from schemas.manufacturers import ManufacturerResponseSchema

if TYPE_CHECKING:
    from instruments import Instruments
    from instr_history import InstrHistory


class Manufacturers(Base):
    __tablename__ = "manufacturers"

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    full_name: Mapped[str] = mapped_column(String(150), nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    instruments: Mapped[list["Instruments"]] = relationship(back_populates="manufacturer")
    instr_history: Mapped[list["InstrHistory"]] = relationship(back_populates="manufacturer")

    def to_read_model(self) -> "ManufacturerResponseSchema":
        return ManufacturerResponseSchema(
            id=self.id,
            name=self.name,
            full_name=self.full_name,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
