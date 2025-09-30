from utils.unitofwork import IUnitOfWork
from schemas.ints_points import InstPointAddSchema, InstPointEditSchema


class InstPointsService:

    async def get_inst_points(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.inst_points.find_all()
            return res


    async def get_inst_points_with_dept(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.inst_points.find_all_with_dept()
            return res


    async def get_inst_point(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.inst_points.find_one(params=params)
            return res


    async def get_inst_point_with_dept(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.inst_points.find_one_with_dept(params=params)
            return res


    async def add_inst_point(self, uow: IUnitOfWork, schema: InstPointAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.inst_points.add_one(res_dict)
            await uow.commit()
            return id


    async def edit_inst_point(self, uow: IUnitOfWork, params: dict, schema: InstPointEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.inst_points.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete_inst_point(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.inst_points.delete(params=params)
            await uow.commit()
