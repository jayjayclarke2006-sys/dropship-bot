import os
import time
import requests

from app.product_research import find_products
from app.listing_generator import generate_listing
from app.supplier_connector import get_supplier_match
from app.amazon_sp_api import submit_listing_to_amazon

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("🚀 AMAZON PREP BOT STARTING...")


def send_message(text):
    if not TOKEN or not CHAT_ID:
        print("Telegram not configured")
        print(text)
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    res = requests.post(url, data=data)
    print("Telegram response:", res.text)


def format_message(product, listing, supplier, amazon_result):
    return f"""
🔥 *AUTO LISTING CANDIDATE*

📦 *Product:* {product['name']}

💰 *Amazon Price:* ${product.get('amazon_price', 'N/A')}
🏷 *Supplier Cost:* ${supplier['total_cost']}
📈 *Estimated Profit:* ${product.get('profit', 'N/A')}
📊 *Score:* {product.get('score', 'N/A')}
⚠️ *Risk:* {product.get('risk', 'unknown')}

🛒 *Supplier Search:*
{supplier['supplier_url']}

━━━━━━━━━━━━━━━
📝 *Generated Listing*

*Title:*
{listing['title']}

*Price:*
${listing['price']}

*Bullets:*
• {listing['bullets'][0]}
• {listing['bullets'][1]}
• {listing['bullets'][2]}
• {listing['bullets'][3]}
• {listing['bullets'][4]}

*Description:*
{listing['description']}

━━━━━━━━━━━━━━━
🤖 *Amazon Status:*
{amazon_result['reason']}
"""


def run_bot():
    while True:
        print("🔍 Finding products...")

        try:
            products = find_products()

            if not products:
                send_message("⚠️ No strong products found this scan.")
            else:
                for product in products[:3]:
                    supplier = get_supplier_match(product)
                    listing = generate_listing(product)
                    amazon_result = submit_listing_to_amazon(product, listing)

                    print("📦 Product:", product["name"])
                    print("📝 Listing:", listing["title"])
                    print("🤖 Amazon:", amazon_result["reason"])

                    message = format_message(
                        product,
                        listing,
                        supplier,
                        amazon_result
                    )

                    send_message(message)

        except Exception as e:
            print("ERROR:", e)
            send_message(f"❌ Bot error: {e}")

        print("⏳ Waiting 10 minutes...\n")
        time.sleep(600)


if __name__ == "__main__":
    run_bot()
