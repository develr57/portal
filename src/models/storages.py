from typing import TYPE_CHECKING
from models.base import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from schemas.storages import StorageResponseSchema, StorageResponseSchemaWithDeptAndObject

if TYPE_CHECKING:
    from departments import Departments
    from instruments import Instruments
    from objects import Objects


class Storages(Base):
    __tablename__ = "storages"

    id: Mapped[int_pk]
    storage: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(150), nullable=True)
    dept_id: Mapped[int] = mapped_column(ForeignKey("departments.id", ondelete="RESTRICT"))
    object_id: Mapped[int] = mapped_column(ForeignKey("objects.id", ondelete="RESTRICT"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    department: Mapped["Departments"] = relationship(back_populates="storages")
    instruments: Mapped[list["Instruments"]] = relationship(back_populates="storage")
    object: Mapped["Objects"] = relationship(back_populates="storages")


    def to_read_model(self) -> "StorageResponseSchema":
        return StorageResponseSchema(
            id=self.id,
            storage=self.storage,
            description=self.description,
            dept_id=self.dept_id,
            object_id=self.object_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


    def to_read_model_with_dept_and_object(self) -> "StorageResponseSchemaWithDeptAndObject":
        return StorageResponseSchemaWithDeptAndObject(
            id=self.id,
            storage=self.storage,
            description=self.description,
            dept_id=self.dept_id,
            object_id=self.object_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            dept_name=self.department.name,
            dept_full_name=self.department.full_name,
            object_name=self.object.name,
            object_full_name=self.object.full_name,
        )
