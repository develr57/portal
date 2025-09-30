from typing import TYPE_CHECKING
from models.base import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from schemas.statuses import StatusResponseSchema

# if TYPE_CHECKING:
#     from departments import Departments
#     from objects import Objects


class Statuses(Base):
    __tablename__ = "statuses"

    id: Mapped[int_pk]
    status: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    # departments: Mapped[list["Departments"]] = relationship(back_populates="company")

    def to_read_model(self) -> "StatusResponseSchema":
        return StatusResponseSchema(
            id=self.id,
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
