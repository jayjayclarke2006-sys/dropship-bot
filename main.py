from fastapi import FastAPI
from app.product_research import find_products
from app.listing_generator import generate_listing
import time

app = FastAPI()


# ✅ Health check
@app.get("/")
def home():
    return {"status": "running"}


# 🔥 Scan products endpoint
@app.get("/scan-products")
def scan_products():
    data = find_products()
    best = data["best_product"]

    if not best:
        return {"status": "no products found"}

    listing = generate_listing(best)

    return {
        "status": "success",
        "best_product": best,
        "listing": listing
    }


# 🔥 Background bot loop
def run_bot():
    while True:
        print("\n🔍 Scanning for products...\n")

        data = find_products()
        best = data["best_product"]

        if best:
            print("🔥 BEST PRODUCT FOUND:")
            print(best)

            listing = generate_listing(best)

            print("\n📝 GENERATED LISTING:")
            print(listing)

        else:
            print("❌ No good products found")

        print("\n⏳ Waiting 10 minutes...\n")
        time.sleep(600)


# 🚀 Start bot when server starts
@app.on_event("startup")
def startup_event():
    import threading
    thread = threading.Thread(target=run_bot)
    thread.start()
