from typing import TYPE_CHECKING
from models.base import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from schemas.units import UnitResponseSchema

if TYPE_CHECKING:
    from instruments import Instruments
    from instr_history import InstrHistory


class Units(Base):
    __tablename__ = "units"

    id: Mapped[int_pk]
    unit: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(150), nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    instruments: Mapped[list["Instruments"]] = relationship(back_populates="unit")
    instr_history: Mapped[list["InstrHistory"]] = relationship(back_populates="unit")

    def to_read_model(self) -> "UnitResponseSchema":
        return UnitResponseSchema(
            id=self.id,
            unit=self.unit,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
