from fastapi import FastAPI
from app.product_research import find_products
from app.listing_generator import generate_listing
from app.telegram_bot import send_telegram_photo
import time
import threading

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


def run_bot():
    while True:
        print("🔍 Scanning for products...")

        products = find_products()

        if not products:
            print("❌ No good products found")
        else:
            top_products = products[:3]

            print(f"🔥 TOP {len(top_products)} PRODUCTS FOUND")

            for i, product in enumerate(top_products, 1):
                listing = generate_listing(product)

                caption = f"""
🏆 <b>TOP PRODUCT #{i}</b>

📦 <b>{product['name']}</b>

💰 Profit: ${product['profit']}
🛒 Price: ${product['amazon_price']}
📊 Score: {product['score']}
📈 Trend: {product['trend_score']}
⚠️ Risk: {product['risk'].upper()}

━━━━━━━━━━━━━━━
🧠 <b>AI LISTING</b>

🏷 {listing['title']}

• {listing['bullets'][0]}
• {listing['bullets'][1]}
• {listing['bullets'][2]}

━━━━━━━━━━━━━━━
🚀 Ready to sell
"""

                print(f"📤 Sending product #{i} to Telegram")

                send_telegram_photo(
                    product["image"],
                    caption
                )

        print("⏳ Waiting 10 minutes...\n")
        time.sleep(600)


threading.Thread(target=run_bot).start()
