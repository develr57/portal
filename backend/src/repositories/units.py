from models.units import Units
from utils.repository import SQLAlchemyRepository


class UnitsRepository(SQLAlchemyRepository):
    model = Units