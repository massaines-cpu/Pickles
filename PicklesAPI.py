from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()



@app.post("/test")
async def test(payload: dict):
    return payload