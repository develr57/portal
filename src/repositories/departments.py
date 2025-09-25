from models.departments import Departments
from utils.repository import SQLAlchemyRepository


class DepartmentsRepository(SQLAlchemyRepository):
    model = Departments