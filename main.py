import time
import os
import requests

from app.supplier_connector import fetch_cj_products

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(text):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text
        }

        r = requests.post(url, json=payload, timeout=30)
        print("Telegram:", r.text)

    except Exception as e:
        print("Telegram error:", e)


def main():
    print("🚀 CJ BOT STARTED")

    while True:
        try:
            products = fetch_cj_products()

            print("FOUND PRODUCTS:", len(products))

            if not products:
                send_telegram_message("❌ No CJ products returned")
            else:
                for p in products:
                    msg = f"""
🔥 {p['title']}

💰 Price: ${p['price']}
📈 Profit: ${p['profit']}
📊 Trend Score: {p['trend_score']}

🖼 {p['image']}
🔗 {p['link']}
"""
                    send_telegram_message(msg)
                    time.sleep(2)

        except Exception as e:
            print("MAIN ERROR:", e)
            send_telegram_message(f"❌ ERROR: {e}")

        print("Sleeping 2 minutes...")
        time.sleep(120)


if __name__ == "__main__":
    main()
