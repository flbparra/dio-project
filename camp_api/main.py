from fastapi import FastAPI
from camp_api.routers import api_rounter


app = FastAPI()
app.include_router(api_rounter)
