from models.instr_types import InstrTypes
from utils.repository import SQLAlchemyRepository


class InstrTypesRepository(SQLAlchemyRepository):
    model = InstrTypes