from fastapi import APIRouter
from api.v1 import router as v1_router
from core.config import settings


router = APIRouter(
    prefix=settings.api.prefix,
)

router.include_router(
    v1_router
)
