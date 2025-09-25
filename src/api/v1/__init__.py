from fastapi import APIRouter
from .companies import router as company_router
from config import settings


router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    company_router,
)
