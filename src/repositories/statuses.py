from models.statuses import Statuses
from utils.repository import SQLAlchemyRepository


class StatusesRepository(SQLAlchemyRepository):
    model = Statuses