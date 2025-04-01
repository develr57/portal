from src.models.companies import Companies
from src.utils.repository import SQLAlchemyRepository


class CompaniesRepository(SQLAlchemyRepository):
    model = Companies