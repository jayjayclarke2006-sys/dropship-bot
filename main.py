from fastapi import FastAPI
from app.product_research import find_products
from app.listing_generator import generate_listing

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


@app.get("/best-product")
def best_product():
    products = find_products()

    if not products:
        return {
            "status": "no products found",
            "message": "No winning products found right now. Try scanning again."
        }

    best = max(products, key=lambda p: p.get("score", 0))
    listing = generate_listing(best)

    return {
        "status": "success",
        "best_product": best,
        "listing": listing
    }


@app.get("/generate-listing")
def generate_product_listing():
    products = find_products()

    if not products:
        return {"status": "no products found"}

    best = max(products, key=lambda p: p.get("score", 0))
    listing = generate_listing(best)

    return {
        "status": "success",
        "product": best,
        "listing": listing
    }
