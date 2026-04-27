from fastapi import FastAPI
from app.product_research import find_products
from app.listing_generator import generate_listing
from app.telegram_bot import send_telegram_message
import time
import threading

# ✅ THIS MUST EXIST
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


# 🔥 BOT LOOP
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

            # 🚀 SEND TO TELEGRAM
            message = f"""
🔥 BEST PRODUCT FOUND

📦 {best['name']}
💰 Profit: ${best['profit']}
📊 Score: {best['score']}
📈 Trend: {best['trend_score']}
⚠️ Risk: {best['risk']}

🛒 Price: ${best['amazon_price']}

-----------------------

📝 LISTING:
{listing['title']}

{listing['description']}
"""
            send_telegram_message(message)

        print("⏳ Waiting 10 minutes...\n")
        time.sleep(600)


# ✅ START BACKGROUND BOT
threading.Thread(target=run_bot).start()
