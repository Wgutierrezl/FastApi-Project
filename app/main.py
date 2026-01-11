from fastapi import FastAPI
from app.controllers.user_controller import router as user_routes
from app.controllers.project_controller import router as project_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine

# Crear tablas
Base.metadata.create_all(bind=engine)

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes)
app.include_router(project_router)