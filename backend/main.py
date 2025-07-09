from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database, routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://flora-steel-three.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(routes.router)
