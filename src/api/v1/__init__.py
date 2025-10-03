from fastapi import APIRouter
from .companies import router as company_router
from .departments import router as department_router
from .employees import router as employee_router
from .inst_points import router as inst_point_router
from .instr_types import router as instr_type_router
from .instruments import router as instrument_router
from .manufacturers import router as manufacturer_router
from .objects import router as object_router
from .statuses import router as status_router
from .storages import router as storage_router
from .units import router as unit_router
from .users import router as user_router
from config import settings


router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(company_router)
router.include_router(department_router)
router.include_router(employee_router)
router.include_router(inst_point_router)
router.include_router(instr_type_router)
router.include_router(instrument_router)
router.include_router(manufacturer_router)
router.include_router(object_router)
router.include_router(status_router)
router.include_router(storage_router)
router.include_router(unit_router)
router.include_router(user_router)
