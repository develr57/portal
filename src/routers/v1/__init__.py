import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from fastapi import APIRouter
from .companies import router as company_router
from src.config import settings


router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    company_router,
)
