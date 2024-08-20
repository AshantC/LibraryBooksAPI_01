from fastapi import FastAPI
from api.v1.endpoints.book import router

app = FastAPI()

app.include_router(router)