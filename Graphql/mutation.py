import strawberry

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_data(self) -> bool:
        return True