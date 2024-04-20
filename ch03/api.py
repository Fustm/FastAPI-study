from fastapi import FastAPI
from todo import todo_router

# new Instance of FastAPI
app = FastAPI()

# welcome route
@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }

app.include_router(todo_router)

