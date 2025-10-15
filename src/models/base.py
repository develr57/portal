import datetime, uuid
from sqlalchemy import MetaData, text, UUID
from sqlalchemy.types import BigInteger, Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column
from core.config import settings
from typing import Annotated


# bigint_pk = Annotated[int, mapped_column(BigInteger, primary_key=True, autoincrement=True)]
int_pk = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]
uuid_pk = Annotated[
    uuid.UUID,
    mapped_column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                        onupdate=datetime.datetime.now(datetime.UTC))]


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=settings.naming_convention)