from fastapi import FastAPI
from routes.mail import mail
app = FastAPI()
app.include_router(mail)
