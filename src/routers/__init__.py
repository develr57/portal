import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from fastapi import APIRouter
from .v1 import router as v1_router
from src.config import settings


router = APIRouter(
    prefix=settings.api.prefix,
)

router.include_router(
    v1_router
)
