from utils.unitofwork import IUnitOfWork
from schemas.users import UserAddSchema, UserEditSchema, UserChangePasswordSchema


class UsersService:

    async def get_all(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.users.find_all()
            return res


    async def get_all_with_emp(self, uow: IUnitOfWork):
        async with uow:
            res = await uow.users.find_all_with_emp()
            return res


    async def get_one(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.users.find_one(params=params)
            return res


    async def get_one_with_emp(self, uow: IUnitOfWork, params: dict):
        async with uow:
            res = await uow.users.find_one_with_emp(params=params)
            return res


    async def add(self, uow: IUnitOfWork, schema: UserAddSchema) -> int:
        res_dict = schema.model_dump()
        async with uow:
            id = await uow.users.add_one(res_dict)
            await uow.commit()
            return id


    async def edit(self, uow: IUnitOfWork, params: dict, schema: UserEditSchema):
        res_dict = schema.model_dump()
        async with uow:
            await uow.users.edit_one(params=params, data=res_dict)
            await uow.commit()


    async def delete(self, uow: IUnitOfWork, params: dict):
        async with uow:
            await uow.users.delete(params=params)
            await uow.commit()
