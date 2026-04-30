import os
import time
import requests

from app.product_research import find_products

# ENV VARIABLES
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Missing Telegram credentials")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, json=payload)
        print("📤 Telegram response:", response.text)
    except Exception as e:
        print("❌ Telegram error:", e)


def format_product(product):
    return f"""
🔥 <b>{product.get('name', 'Unknown Product')}</b>

💰 Price: ${product.get('recommended_price', 'N/A')}
📈 Profit: ${product.get('profit', 'N/A')}
📊 Trend Score: {product.get('trend_score', 'N/A')}
"""


def main():
    print("🚀 Bot started...")

    while True:
        try:
            print("🔍 Fetching products...")

            products = find_products()

            print("RAW PRODUCTS:", products)
            print(f"📦 Found {len(products)} products")

            for product in products:
                msg = format_product(product)
                print("📨 Sending:", msg)

                send_telegram_message(msg)
                time.sleep(2)

            print("✅ Cycle complete — sleeping 5 mins...\n")
            time.sleep(300)

        except Exception as e:
            print("❌ ERROR:", e)
            time.sleep(10)


if __name__ == "__main__":
    main()
