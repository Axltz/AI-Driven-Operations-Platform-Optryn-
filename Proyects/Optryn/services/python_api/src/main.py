from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(
    title="Optryn Core API",
    version="0.1.0", 
    docs_url="/docs"
    )

class HealthResponse(BaseModel):
    status: str

class EchoRequest(BaseModel):
    message: str

DB = {
    1: {"name": "Product A", "price": 10.0},
    2: {"name": "Product B", "price": 20.0},
}

@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="ok")

@app.post("/echo")
async def echo(req: EchoRequest):
    return {"echo": req.message}

@app.get("/products")
async def list_products():
    return DB

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    product = DB.get(product_id)
    if not product:
        return {"error": "Product not found"}
    return product

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
