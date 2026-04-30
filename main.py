import os
import time
import requests

from app.supplier_connector import fetch_cj_products
from app.listing_generator import generate_listing

# ENV VARIABLES
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Telegram error:", e)


def main():
    print("🚀 Bot started...")

    while True:
        try:
            products = fetch_cj_products()

            print(f"Found {len(products)} products")

            if not products:
                print("No products found")
                time.sleep(60)
                continue

            for product in products:
                listing = generate_listing(product)

                message = f"""
🔥 <b>{listing['title']}</b>

{listing['bullets']}

{listing['description']}
"""

                send_telegram_message(message)
                time.sleep(2)

        except Exception as e:
            print("Error:", e)

        time.sleep(300)  # 5 mins


if __name__ == "__main__":
    main()
