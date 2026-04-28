import os
import time
import requests

# 🔥 IMPORTANT: matches your current folder structure (app/app/)
from app.app.product_research import find_products
from app.app.listing_generator import generate_listing
from app.app.supplier_connector import get_supplier_match
from app.app.amazon_sp_api import submit_listing_to_amazon


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("🚀 BOT STARTING...")


# ---------------- TELEGRAM ---------------- #

def send_message(text):
    if not TOKEN or not CHAT_ID:
        print("❌ Telegram not configured")
        print(text)
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        res = requests.post(url, data=data, timeout=10)
        print("Telegram:", res.text)
    except Exception as e:
        print("Telegram error:", e)


# ---------------- FORMAT MESSAGE ---------------- #

def format_message(product, listing, supplier, amazon_result):
    return f"""
🔥 *AUTO PRODUCT FOUND*

📦 *Product:* {product['name']}

💰 *Amazon Price:* ${product.get('amazon_price', 'N/A')}
🏷 *Supplier Cost:* ${supplier['total_cost']}
📈 *Profit:* ${product.get('profit', 'N/A')}
📊 *Score:* {product.get('score', 'N/A')}
⚠️ *Risk:* {product.get('risk', 'unknown')}

🛒 *Supplier Link:*
{supplier['supplier_url']}

━━━━━━━━━━━━━━━
📝 *Listing*

*Title:*
{listing['title']}

*Price:* ${listing['price']}

*Bullets:*
• {listing['bullets'][0]}
• {listing['bullets'][1]}
• {listing['bullets'][2]}
• {listing['bullets'][3]}
• {listing['bullets'][4]}

━━━━━━━━━━━━━━━
🤖 *Amazon Status:*
{amazon_result['reason']}
"""


# ---------------- MAIN LOOP ---------------- #

def run_bot():
    while True:
        print("🔍 Scanning for products...")

        try:
            products = find_products()

            if not products:
                send_message("⚠️ No strong products found this scan.")
            else:
                for product in products[:3]:
                    print("📦 Found:", product["name"])

                    supplier = get_supplier_match(product)
                    listing = generate_listing(product)
                    amazon_result = submit_listing_to_amazon(product, listing)

                    message = format_message(
                        product,
                        listing,
                        supplier,
                        amazon_result
                    )

                    send_message(message)

        except Exception as e:
            print("❌ ERROR:", e)
            send_message(f"❌ Bot crashed: {e}")

        print("⏳ Waiting 10 minutes...\n")
        time.sleep(600)


# ---------------- START ---------------- #

if __name__ == "__main__":
    run_bot()
