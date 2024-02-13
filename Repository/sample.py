from Model.sample import Sample
from config import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete


class SampleRepository:
    @staticmethod
    async def create(sample_data: Sample):
        async with db as session:
            async with session.begin():
                session.add(sample_data)
            await db.commit_rollback()

    @staticmethod
    async def get_by_id(id: int):
        async with db as session:
            stmt = select(Sample).where(Sample.id == id)
            result = await session.execute(stmt)
            sample = result.scalars().first()
            return sample

    @staticmethod
    async def get_by_name(name: str):
        async with db as session:
            stmt = select(Sample).where(Sample.name == name)
            result = await session.execute(stmt)
            sample = result.scalar_one_or_none()
            return sample
        

    @staticmethod
    async def get_all():
        async with db as session:
            stmt = select(Sample)
            result = await session.execute(stmt)
            return result.scalars().all()

    @staticmethod
    async def update(sample_id: int, sample_data: Sample):
        async with db as session:
            stmt = select(Sample).where(Sample.id == sample_id)
            result = await session.execute(stmt)
            sample = result.scalars().first()
            sample.name = sample_data.name

            query = (
                sql_update(Sample)
                .where(Sample.id == sample_id)
                .values(**sample.dict())
                .execution_options(synchronize_session="fetch")
            )

            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(sample_id: int):
        async with db as session:
            query = sql_delete(Sample).where(Sample.id == sample_id)
            await session.execute(query)
            await db.commit_rollback()
