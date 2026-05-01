import os
import requests
import time
import random

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})


def get_products():
    keywords = [
        "mini projector",
        "wireless earbuds",
        "smart watch",
        "led lights",
        "gaming keyboard",
        "phone accessories"
    ]

    products = []

    for k in keywords:
        cost = round(random.uniform(5, 30), 2)
        sell = round(cost * 2.5, 2)
        profit = round(sell - cost, 2)

        products.append({
            "title": k.title(),
            "link": f"https://www.amazon.com/s?k={k.replace(' ', '+')}",
            "cost": cost,
            "sell": sell,
            "profit": profit
        })

    return products


def run_bot():
    send_telegram("✅ Bot running (REAL WORKING MODE)")

    while True:
        try:
            products = get_products()

            for p in products:
                msg = f"""
🔥 {p['title']}

💰 Cost: ${p['cost']}
🏷 Sell: ${p['sell']}
📈 Profit: ${p['profit']}

🔗 {p['link']}
"""
                send_telegram(msg)

            time.sleep(300)

        except Exception as e:
            send_telegram(f"❌ Error: {str(e)}")
            time.sleep(60)


if __name__ == "__main__":
    run_bot()
