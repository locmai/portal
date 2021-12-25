from typing import Type
from repositories.base import BaseRepository
from schemas.base import BaseSchema

class BaseService:
    def __init__(self, repo: BaseRepository):
        self._repo = repo
    
    @property
    def repo(self) -> BaseRepository:
        return self._repo
    
    async def get(self):
        return await self.repo.get(self)
    
    async def get_by_id(self, id):
        return await self.repo.get_by_id(self, id)

    async def create(self, schema: BaseSchema):
        return await self.repo.create(self, schema)

class ExtendedService:
    pass