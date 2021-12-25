from fastapi import APIRouter
from .org import router as org_router
from loguru import logger

@logger.catch
def get_router():
    router = APIRouter()
    router.include_router(org_router,prefix='/orgs')
    return router