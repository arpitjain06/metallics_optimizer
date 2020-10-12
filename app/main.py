from fastapi import FastAPI
from app.api.routes.chemical import chemical
from app.api.routes.commodity import commodity
from app.api.routes.composition import composition
from app.api.db import metadata, database, engine

from app.api.repository.scripts import migrations
app = FastAPI()

metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()
    await migrations()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(chemical, prefix='/api/v1/chemical', tags=['Chemical'])
app.include_router(commodity, prefix='/api/v1/commodity', tags=['Commodity'])
app.include_router(
    composition, prefix='/api/v1/composition', tags=['Chemical concentration'])
