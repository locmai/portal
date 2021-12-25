from fastapi import APIRouter, Depends

from repositories.orgs import OrgRepository
from services.orgs import OrgService
from schemas.orgs import OrgSchema
from core.database import get_repository
from loguru import logger
from typing import List
import json

router = APIRouter()
@router.get('/', response_model=List[OrgSchema])
async def get_orgs(org_svc: OrgService = Depends(OrgService)):
    orgs = await org_svc.get()

    org_results = []
    for org in orgs:
        org_results.append(OrgScema(**org))

    return org_results