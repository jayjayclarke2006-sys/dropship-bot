from fastapi import FastAPI
from app.product_research import find_products
from app.listing_generator import generate_listing
import threading
from app.scheduler import run_bot

app = FastAPI()


# ✅ Home route
@app.get("/")
def home():
    return {"status": "running"}


# ✅ Scan products
@app.get("/scan-products")
def scan_products():
    results = find_products()
    return {
        "status": "success",
        "products_found": len(results),
        "products": results
    }


# ✅ Get best product + listing
@app.get("/best-product")
def best_product():
    products = find_products()

    if not products:
        return {"status": "no products found"}

    best = products[0]
    listing = generate_listing(best)

    return {
        "status": "success",
        "product": best,
        "listing": listing
    }


# ✅ Start automation bot (background)
threading.Thread(target=run_bot, daemon=True).start()
