import uvicorn
from fastapi import FastAPI
from test_routes import test_router

app = FastAPI()

app.include_router(test_router)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
