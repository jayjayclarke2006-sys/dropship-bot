from fastapi import FastAPI
from app.product_research import find_products
from app.listing_generator import generate_listing
import time

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/scan-products")
def scan_products():
    products = find_products()
    return {
        "status": "success",
        "products_found": len(products),
        "products": products
    }


# 🔥 AUTO ENGINE LOOP
def run_bot():
    while True:
        print("🔍 Scanning for products...")

        products = find_products()

        if not products:
            print("❌ No good products found")
        else:
            best = products[0]
            print("🔥 BEST PRODUCT FOUND:", best)

            listing = generate_listing(best)
            print("📦 GENERATED LISTING:", listing)

        print("⏳ Waiting 10 minutes...\n")
        time.sleep(600)


# Run in background
import threading
threading.Thread(target=run_bot).start()
