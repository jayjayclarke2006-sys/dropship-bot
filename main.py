import os
import time
import requests

from app.product_research import find_products


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


def format_product(product):
    return f"""
🔥 <b>{product['title']}</b>

💰 Price: £{product['price']}
📦 Sales: {product['sales']}

🔗 {product['link']}
"""


def main():
    print("🚀 Bot started...")

    while True:
        try:
            products = find_products()

            print(f"Found {len(products)} products")

            for product in products:
                msg = format_product(product)
                send_telegram_message(msg)
                time.sleep(2)

        except Exception as e:
            print("Error:", e)

        # wait before next scan
        time.sleep(300)  # 5 minutes


if __name__ == "__main__":
    main()
