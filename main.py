from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import start_db
from Routers.birds import router as birds_router
from Routers.birdspotting import router as birdspotting_router
from Routers.species import router as species_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    start_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(birds_router)
app.include_router(birdspotting_router)
app.include_router(species_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}