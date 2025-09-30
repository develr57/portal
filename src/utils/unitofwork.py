from abc import ABC, abstractmethod
from typing import Type

from database import async_session_factory
from repositories.companies import CompaniesRepository
from repositories.departments import DepartmentsRepository
from repositories.manufacturers import ManufacturersRepository
from repositories.objects import ObjectsRepository
from repositories.types import TypesRepository


# https://github1s.com/cosmicpython/code/tree/chapter_06_uow
class IUnitOfWork(ABC):
    companies: Type[CompaniesRepository]
    departments: Type[DepartmentsRepository]
    objects: Type[ObjectsRepository]
    manufacturers: Type[ManufacturersRepository]
    types: Type[TypesRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.companies = CompaniesRepository(self.session)
        self.departments = DepartmentsRepository(self.session)
        self.manufacturers = ManufacturersRepository(self.session)
        self.objects = ObjectsRepository(self.session)
        self.types = TypesRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()