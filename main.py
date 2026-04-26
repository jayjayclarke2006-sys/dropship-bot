from fastapi import FastAPI
from app.product_research import find_products

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}


@app.get("/scan-products")
def scan_products():
    results = find_products()
    return {
        "status": "success",
        "products_found": len(results),
        "products": results
    }
