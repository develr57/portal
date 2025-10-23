from models.manufacturers import Manufacturers
from utils.repository import SQLAlchemyRepository


class ManufacturersRepository(SQLAlchemyRepository):
    model = Manufacturers