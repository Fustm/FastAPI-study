from fastapi import FastAPI

# new Instance of FastAPI
app = FastAPI()

# welcome route
@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }