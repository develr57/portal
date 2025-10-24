from urllib import request

from fastapi import APIRouter, Request, Depends
# from fastapi.params import Depends
from api.dependencies import UOWDep
from schemas.auth_tokens import TokenInfoSchema
from schemas.users import UserAddSchema, UserEditSchema
from services.users import UsersService
from utils.jwt_utils import (
    validate_auth_user, UserSchema, get_current_active_auth_user, get_current_token_payload, create_access_token,
    create_refresh_token, get_current_auth_user_for_refresh
)
from utils.unitofwork import IUnitOfWork


router = APIRouter(prefix="/auth", tags=["Auth"], )


@router.post("/login/", response_model=TokenInfoSchema)
async def login(
        uow: UOWDep,
        user: UserEditSchema = Depends(validate_auth_user)
):
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return TokenInfoSchema(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.get("/user_me")
async def get_me(
    uow: UOWDep,
    user: UserSchema = Depends(get_current_active_auth_user),
    payload: dict = Depends(get_current_token_payload),
):
    iat = payload.get("iat")
    return {
        "username": user.username,
        "email": user.email,
        "logged_ia_at": iat
    }


@router.post("/refresh/", response_model=TokenInfoSchema)
async def refresh_jwt(
    user: UserSchema = Depends(get_current_auth_user_for_refresh),
):
    access_token = create_access_token(user)
    return TokenInfoSchema(
        access_token=access_token,
    )


# @router.get("/test")
# async def test(req: Request = None):
#     print("request: ", req.headers)
