from typing import Any, Optional, List, Tuple, Type

from loguru import logger

from sqlalchemy.orm import Session
from schemas.base import BaseSchema
from models.base import Base

def _log_query(query: str, query_params: Tuple[Any, ...]) -> None:
    logger.debug("query: {0}, values: {1}", query, query_params)


class BaseRepository:
    def __init__(self, db: Session, model: Base ) -> None:
        self._db: Session = db
        self._schema = schema

    async def get(self, skip: int = 0, limit: int = 100) -> List[Any]:
        return self._db.query(self._schema).offset(skip).limit(limit).all()

    async def get_by_id(self, id: int) -> Optional[Any]:
        return self._db.query(self._schema).filter(self._schema.id == id).first()

    async def create(self, schema: BaseSchema) -> BaseSchema:
        db_obj = schema
        self._db.add(db_obj)
        self._db.commit()
        self._db.refresh(db_obj)
        return db_obj
