from models.types import Types
from utils.repository import SQLAlchemyRepository


class TypesRepository(SQLAlchemyRepository):
    model = Types