from typing import Optional
from sqlmodel import SQLModel, Field

class Sample(SQLModel, table=True):
    __tablename__ = "sample"

    id: Optional[int] = Field(None, primary_key=True, nullable=True)
    name: str
