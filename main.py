import time
import os
import requests

from app.supplier_connector import fetch_cj_products

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }

    r = requests.post(url, json=payload)
    print("Telegram:", r.text)


def main():
    print("🚀 CJ TEST STARTED")

    while True:
        try:
            products = fetch_cj_products()

            print("CJ PRODUCTS:", products)

            if not products:
                send_telegram_message("❌ No CJ products returned")
            else:
                for p in products:
                    msg = f"""
🔥 {p.get('title')}

💰 Price: {p.get('price')}
📈 Profit: {p.get('profit')}
🖼 {p.get('image')}
🔗 {p.get('link')}
"""
                    send_telegram_message(msg)
                    time.sleep(2)

        except Exception as e:
            print("ERROR:", e)
            send_telegram_message(f"❌ ERROR: {e}")

        time.sleep(120)


if __name__ == "__main__":
    main()
