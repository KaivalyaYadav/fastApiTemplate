from typing import List, Dict
import strawberry
from schema import (
    SampleType
)

from Service.sample import SampleService

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World!"
    
    @strawberry.field
    async def get_all_samples(self) -> List[SampleType]:
        return await SampleService.get_all_samples()