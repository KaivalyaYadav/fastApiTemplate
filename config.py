import os

from sqlalchemy.sql import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from dotenv import load_dotenv
from typing import AsyncGenerator

load_dotenv()

DB_CONFIG = os.getenv("LOCAL_DB_CONFIG")


class DatabaseSession:
    def __init__(self, url: str = DB_CONFIG):
        self.engine = create_async_engine(
            url,
            echo=False,
            pool_size=10,
            max_overflow=-1,
        )
        self.SessionLocal = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )

    # Generating models into a database
    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    # Drop models into a database
    async def drop_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)

    # close connection
    async def close(self):
        await self.engine.dispose()

    # Prepare the context for the asynchronous operation
    async def __aenter__(self) -> AsyncSession:
        self.session = self.SessionLocal()
        return self.session

    # clean up resources etc
    async def __aexit__(self, exc_type, esc_val, exc_tb):
        await self.session.close()


    async def get_db(self) -> AsyncGenerator[AsyncSession, None]:
        async with self as db:
            yield db


    async def commit_rollback(self):
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise


db = DatabaseSession()
