import strawberry
from typing import List
from datetime import datetime

@strawberry.type
class SampleType:
    id: int
    name: str

@strawberry.input
class SampleInput:
    name: str
