from typing import Callable
from fastapi import FastAPI
from loguru import logger
from core.database import connect_to_db, close_db_connections


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    async def start_app() -> None:
        await connect_to_db(app)
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    async def stop_app() -> None:
        await close_db_connections(app)

    return stop_app
