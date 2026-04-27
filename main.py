from fastapi import FastAPI
from app.product_research import find_products
from app.listing_generator import generate_listing

app = FastAPI()

# -------------------------------
# Health Check
# -------------------------------
@app.get("/")
def home():
    return {"status": "running"}

# -------------------------------
# Scan Products
# -------------------------------
@app.get("/scan-products")
def scan_products():
    results = find_products()

    return {
        "status": "success",
        "products_found": len(results),
        "products": results
    }

# -------------------------------
# Generate Listing
# -------------------------------
@app.get("/generate-listing")
def generate_product_listing():
    products = find_products()

    if not products:
        return {"status": "no products found"}

    product = products[0]  # take best product

    listing = generate_listing(product)

    return {
        "status": "success",
        "product": product,
        "listing": listing
    }
