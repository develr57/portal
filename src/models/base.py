import datetime

from sqlalchemy import MetaData, text
from sqlalchemy.types import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.config import settings
from typing import Annotated


bigint_pk = Annotated[int, mapped_column(BigInteger, primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                        onupdate=datetime.datetime.now(datetime.UTC))]


class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention=settings.naming_convention
    )