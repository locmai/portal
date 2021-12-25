from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from core.config import SQLALCHEMY_DATABASE_URI
from core.config import DEBUG
from repositories.base import BaseRepository
from typing import Callable, Type, Any
from starlette.requests import Request
from fastapi import Depends, FastAPI
from loguru import logger
from sqlalchemy.ext.declarative import declarative_base


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Initializing session ...")
    engine = create_engine(
        SQLALCHEMY_DATABASE_URI,
        echo=DEBUG,
        pool_pre_ping=True)
    declarative_base().metadata.create_all(engine)
    app.state.session: Session = Session(engine)
    logger.info("app.state.session initialized.")


async def close_db_connections(app: FastAPI) -> None:
    logger.info("Closing connections to database")
    app.state.session.close_all()
    logger.info("Connections are closed")


def _get_session(request: Request) -> Session:
    return request.app.state.session


def get_repository(repo: BaseRepository) -> Callable:  # type: ignore
    async def _get_repository(session: Session = Depends(_get_session)):
        return repo(session)
    return _get_repository
