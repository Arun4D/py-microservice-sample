from fastapi import FastAPI
from app.api.customer import customers
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/customer/openapi.json", docs_url="/api/v1/customer/docs")


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(customers, prefix='/api/v1/customer', tags=['customers'])
