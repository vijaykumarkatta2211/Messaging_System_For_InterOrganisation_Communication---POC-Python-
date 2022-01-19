from fastapi import FastAPI
from routes.user import org
app = FastAPI()
app.include_router(org)
