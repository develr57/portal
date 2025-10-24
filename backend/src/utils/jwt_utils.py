from datetime import timedelta, datetime, timezone

from fastapi import HTTPException, status, Form, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer

from core.config import BASE_DIR, settings
import jwt, bcrypt
from jwt import InvalidTokenError


# http_bearer = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")
jwt_private_key_path = BASE_DIR / settings.JWT_PRIVATE_KEY_PATH
jwt_public_key_path = BASE_DIR / settings.JWT_PUBLIC_KEY_PATH

def encode_jwt(
        payload: dict,
        private_key: str = jwt_private_key_path.read_text(),
        algorithm: str = settings.JWT_ALGORITHM,
        expire_minutes: int = settings.JWT_ACCESS_TOKEN_EXPIRES_MINUTES,
        expire_timedelta: timedelta | None = None
):
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)
    if expire_timedelta:
        expire = now + expire_timedelta
        print("if", expire)
    else:
        expire = now + timedelta(minutes=expire_minutes)
        print("else ", expire)
    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(
        payload=to_encode,
        key=private_key,
        algorithm=algorithm,
    )
    print("encode_jwt - return")
    return encoded


def decode_jwt(
        token: str | bytes,
        public_key: str = jwt_public_key_path.read_text(),
        algorithm: str = settings.JWT_ALGORITHM,
):
    decoded = jwt.decode(
        jwt=token,
        key=public_key,
        algorithms=[algorithm],
    )
    return decoded


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password)


def validate_auth_user(
        username: str = Form(),
        password: str = Form(),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password",
    )
    if not (user := users_db.get(username)):
        raise unauthed_exc
    if not validate_password(password=password, hashed_password=user.password):
        raise unauthed_exc
    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user inactive",
        )
    return user


from pydantic import BaseModel, EmailStr, ConfigDict

TOKEN_TYPE_FIELD = "type"
ACCESS_TOKEN_TYPE = "access"
REFRESH_TOKEN_TYPE = "refresh"


class UserSchema(BaseModel):
    username: str
    password: bytes
    email: EmailStr | None = None
    active: bool = True

    model_config = ConfigDict(strict=True)


john = UserSchema(
    username="john",
    password=hash_password("qwerty"),
    email="john@example.com",
    active=True,
)

sam = UserSchema(
    username="sam",
    password=hash_password("qwerty"),
    email="sam@example.com",
    active=True,
)

users_db: dict[str, UserSchema] = {
    john.username: john,
    sam.username: sam,
}


def get_current_token_payload(
    # credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
    token: str = Depends(oauth2_scheme),
) -> UserSchema:
    # token = credentials.credentials
    try:
        payload = decode_jwt(token=token)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error: {e}",
        )
    print("get_current_token_payload: ", payload)
    return payload


def validate_token_type(payload: dict, token_type: str) -> bool:
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    print("current_token_type: ", current_token_type, "\ntoken_type: ", token_type)
    if current_token_type == token_type:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"invalid token type {current_token_type!r} expected {token_type!r}",
    )


def get_user_by_token_sub(payload: dict) -> UserSchema:
    print("get_user_by_token_sub - payload: ", payload)
    username: str | None = payload.get("sub", None)
    print("username: ", username)
    if user := users_db.get(username):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid (user not found)",
    )


def get_current_auth_user(
    payload: dict = Depends(get_current_token_payload),
) -> UserSchema:
    validate_token_type(payload=payload, token_type=ACCESS_TOKEN_TYPE)
    return get_user_by_token_sub(payload=payload)



def get_current_auth_user_for_refresh(
    payload: dict = Depends(get_current_token_payload),
) -> UserSchema:
    validate_token_type(payload=payload, token_type=REFRESH_TOKEN_TYPE)
    return get_user_by_token_sub(payload=payload)



def get_current_active_auth_user(
    user: UserSchema = Depends(get_current_auth_user),
):
    print(user)
    if user.active:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="user inactive",
    )


def create_jwt(
    token_type: str,
    token_data: dict,
    expire_minutes: int = settings.JWT_ACCESS_TOKEN_EXPIRES_MINUTES,
    expire_timedelta: timedelta | None = None,
) -> str:
    jwt_payload = {"type": token_type}
    jwt_payload.update(token_data)
    return encode_jwt(
        payload=jwt_payload,
        expire_minutes=expire_minutes,
        expire_timedelta=expire_timedelta,
    )


def create_access_token(user: UserSchema) -> str:
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    return create_jwt(
        token_type=ACCESS_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_minutes=settings.JWT_ACCESS_TOKEN_EXPIRES_MINUTES,
    )


def create_refresh_token(user: UserSchema) -> str:
    jwt_payload = {
        "sub": user.username,
    }
    return create_jwt(
        token_type=REFRESH_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_timedelta=timedelta(days=settings.JWT_REFRESH_TOKEN_EXPIRES_DAYS),
    )