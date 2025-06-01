from typing import TYPE_CHECKING
from src.models.base import Base, bigint_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from sqlalchemy.types import BigInteger

if TYPE_CHECKING:
    from src.models.companies import Companies


class Departments(Base):
    __tablename__ = "departments"

    id: Mapped[bigint_pk]
    name: Mapped[str] = mapped_column(String(100))
    full_name: Mapped[str] = mapped_column(String(150))
    company_id: Mapped[BigInteger] = mapped_column(ForeignKey("companies.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    company: Mapped["Companies"] = relationship(back_populates="departments")
