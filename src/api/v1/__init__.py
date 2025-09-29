from fastapi import APIRouter
from .companies import router as company_router
from .departments import router as department_router
from .objects import router as object_router
from config import settings


router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(company_router)
router.include_router(department_router)
router.include_router(object_router)
