from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiV1Prefix:
    prefix: str = "/v1"

class ApiPrefix:
     prefix: str = "/api"
     v1: ApiV1Prefix = ApiV1Prefix()


class Settings(BaseSettings):
    APP_NAME: str
    APP_DESCRIPTION: str | None

    # authentication
    SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRES_MINUTES: int
    JWT_REFRESH_TOKEN_EXPIRES_DAYS: int
    # Если количество текущих пользовательских сеансов больше, чем значение этой переменной, то все сеансы отменяются
    USER_MAX_ACTIVE_SESSIONS: int

    # DB parameters
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DBMS: str

    # Postgresql
    POOL_SIZE: int
    MAX_OVERFLOW: int

    # redis params
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_AUTH_DB: int
    REDIS_WS_DB: int
    REDIS_PASSWORD: str
    REDIS_PREFIX: str
    REDIS_MAX_CONNECTIONS: int
    REDIS_MIN_CONNECTIONS: int
    REDIS_MAX_IDLE_TIME: int
    REDIS_MAX_ACTIVE_TIME: int
    REDIS_CONNECTION_TIMEOUT: int

    @property
    def ASYNC_DATABASE_URL(self) -> str:
        if self.DBMS == "postgresql":
            # postgresql+asyncpg://user:password@localhost:5432/bn_name
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        else:
            return f"sqlite+aiosqlite:///{self.DB_NAME}.db"

    @property
    def SYNC_DATABASE_URL(self) -> str:
        if self.DBMS == "postgresql":
            # postgresql+psycopg://postgres:postgres@localhost:5432/sa
            return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        else:
            return f"sqlite:///{self.DB_NAME}.db"

    model_config = SettingsConfigDict(env_file="./src/.env")
    api: ApiPrefix = ApiPrefix()
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


settings = Settings()
