from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from TodoApp import models
from TodoApp.database import engine
from TodoApp.routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static")

app.include_router(auth.router)
app.include_router(todos.router)
