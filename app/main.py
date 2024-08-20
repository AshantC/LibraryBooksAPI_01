from fastapi import FastAPI
from src.api.v1.endpoints.book import router

app = FastAPI()

app.include_router(router)