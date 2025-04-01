from src.models.departments import Departments
from src.utils.repository import SQLAlchemyRepository


class DepartmentsRepository(SQLAlchemyRepository):
    model = Departments