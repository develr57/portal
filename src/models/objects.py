from typing import TYPE_CHECKING
from models.base import Base, created_at, updated_at, uuid_pk, int_pk
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from schemas.objects import ObjectResponseSchema, ObjectResponseSchemaWithCompany

if TYPE_CHECKING:
    from companies import Companies


class Objects(Base):
    __tablename__ = "objects"

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    full_name: Mapped[str] = mapped_column(String(150), nullable=True)
    company_id: Mapped[uuid_pk] = mapped_column(ForeignKey("companies.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    company: Mapped["Companies"] = relationship(back_populates="objects")

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
