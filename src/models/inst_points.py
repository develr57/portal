from typing import TYPE_CHECKING
from models.base import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from schemas.ints_points import InstPointResponseSchema, InstPointResponseSchemaWithDeptAndObject

if TYPE_CHECKING:
    from departments import Departments
    from objects import Objects


class InstPoints(Base):
    __tablename__ = "inst_points"

    id: Mapped[int_pk]
    point: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(150), nullable=True)
    dept_id: Mapped[int_pk] = mapped_column(ForeignKey("departments.id", ondelete="CASCADE"))
    object_id: Mapped[int_pk] = mapped_column(ForeignKey("objects.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    department: Mapped["Departments"] = relationship(back_populates="inst_points")
    object: Mapped["Objects"] = relationship(back_populates="inst_points")

    def to_read_model(self) -> "InstPointResponseSchema":
        return InstPointResponseSchema(
            id=self.id,
            point=self.point,
            description=self.description,
            dept_id=self.dept_id,
            object_id=self.object_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


    def to_read_model_with_dept(self) -> "InstPointResponseSchemaWithDeptAndObject":
        return InstPointResponseSchemaWithDeptAndObject(
            id=self.id,
            point=self.point,
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
