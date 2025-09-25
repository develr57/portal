from models.companies import Companies
from utils.repository import SQLAlchemyRepository


class CompaniesRepository(SQLAlchemyRepository):
    model = Companies