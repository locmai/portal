from services.base import BaseService, ExtendedService
from repositories.orgs import OrgRepository
from fastapi import Depends
from core.database import get_repository

class OrgService(BaseService, ExtendedService):
    def __init__(self, repo: OrgRepository = Depends(get_repository(OrgRepository))):
        super().__init__(repo)

    async def create_org(self, schema):
        self.repo.create(self, schema)