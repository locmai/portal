from schemas.orgs import OrgSchema
from sqlalchemy.orm import Session
from repositories.base import BaseRepository


class OrgRepository(BaseRepository):
    def __init__(self, database: Session) -> None:
        super().__init__(database, schema=OrgSchema)
