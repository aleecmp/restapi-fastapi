from fastapi import FastAPI
from routes import user

app = FastAPI(
    title="FastAPI CRUD",
    description="A simple CRUD API built with FastAPI",
    version="0.1.0",
    openapi_tags=[
        {
            "name": "Users",
            "description": "Operations with users",
        }
    ],
)

app.include_router(user.user)
