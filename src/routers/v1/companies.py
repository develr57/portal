from fastapi import APIRouter


router = APIRouter(prefix="/companies", tags=["companies"])


@router.get(path="")
async def get_companies():
    return {"companies": "our company"}