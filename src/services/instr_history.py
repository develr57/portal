from utils.unitofwork import IUnitOfWork
from schemas.instr_history import InstrHistoryAddSchema


class InstrHistoryService:

    async def get_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.instr_history.find_all()
            return res


    async def get_all_with_other(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.instr_history.find_all_with_other()
            return res


    async def get_one(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.instr_history.find_one(params=params)
            return res


    async def get_one_with_other(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.instr_history.find_one_with_other(params=params)
            return res


    async def add(self, uow: IUnitOfWork, schema: InstrHistoryAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.instr_history.add_one(res_dict)
            await uow.commit()
            return id
