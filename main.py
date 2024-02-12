import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from config import DatabaseSession
import strawberry
from Graphql.query import Query
from Graphql.mutation import Mutation

from strawberry.fastapi import GraphQLRouter

def init_app():
    db = DatabaseSession()
    apps = FastAPI(
        title="Fast API Template",
        description="Fast API",
        version="1.0.0"
    )

    # Enable CORS for all routes
    apps.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # You may want to restrict this to specific origins in a production environment
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    logging.basicConfig(level=logging.INFO)

    @apps.on_event("startup")
    async def startup():
        await db.create_all()

    @apps.on_event("shutdown")
    async def shutdown():
        await db.close()

    @apps.get('/')
    def home():
        return "Welcome home!"

    # add graphql endpoint
    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema)

    apps.include_router(graphql_app, prefix="/graphql")

    return apps

app = init_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8888, reload=True, log_level="info")
