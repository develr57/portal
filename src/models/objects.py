from typing import TYPE_CHECKING
from models.base import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from models.instr_history import InstrHistory
from schemas.objects import ObjectResponseSchema, ObjectResponseSchemaWithCompany

if TYPE_CHECKING:
    from companies import Companies
    from inst_points import InstPoints
    from instruments import Instruments
    from instr_history import InstrHistory
    from storages import Storages


class Objects(Base):
    __tablename__ = "objects"

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    full_name: Mapped[str] = mapped_column(String(150), nullable=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id", ondelete="RESTRICT"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    company: Mapped["Companies"] = relationship(back_populates="objects")
    inst_points: Mapped[list["InstPoints"]] = relationship(back_populates="object")
    instruments_as_inst_objects: Mapped[list["Instruments"]] = relationship(
        "Instruments", foreign_keys="[Instruments.inst_object_id]", back_populates="inst_object")
    instruments_as_stor_objects: Mapped[list["Instruments"]] = relationship(
        "Instruments", foreign_keys="[Instruments.stor_object_id]", back_populates="stor_object")
    instr_history_as_inst_objects: Mapped[list["InstrHistory"]] = relationship(
        "InstrHistory", foreign_keys="[InstrHistory.inst_object_id]", back_populates="inst_object")
    instr_history_as_stor_objects: Mapped[list["InstrHistory"]] = relationship(
        "InstrHistory", foreign_keys="[InstrHistory.stor_object_id]", back_populates="stor_object")
    storages: Mapped[list["Storages"]] = relationship(back_populates="object")


    def to_read_model(self) -> "ObjectResponseSchema":
        return ObjectResponseSchema(
            id=self.id,
            name=self.name,
            full_name=self.full_name,
            company_id=self.company_id,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


    def to_read_model_with_company(self) -> "ObjectResponseSchemaWithCompany":
        return ObjectResponseSchemaWithCompany(
            id=self.id,
            name=self.name,
            full_name=self.full_name,
            company_id=self.company_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            company_name=self.company.name,
            company_full_name=self.company.full_name
        )
