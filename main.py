import os
import requests
import time
from bs4 import BeautifulSoup
import random

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})


def fetch_products():
    keywords = [
        "projector",
        "earbuds",
        "smart watch",
        "led lights",
        "gaming keyboard"
    ]

    keyword = random.choice(keywords)
    url = f"https://cjdropshipping.com/search?q={keyword}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        products = []

        items = soup.select(".product-card")

        for item in items[:5]:
            title = item.select_one(".product-title")
            img = item.select_one("img")

            title_text = title.text.strip() if title else "Trending Product"
            img_url = img["src"] if img else ""

            cost = round(random.uniform(5, 25), 2)
            sell = round(cost * 2.2, 2)
            profit = round(sell - cost, 2)

            products.append({
                "title": title_text[:80],
                "cost": cost,
                "sell": sell,
                "profit": profit,
                "image": img_url
            })

        return products

    except:
        return []


def run_bot():
    send_telegram("✅ Bot started (SCRAPER MODE)")

    while True:
        try:
            products = fetch_products()

            if not products:
                send_telegram("❌ Scraper failed, retrying...")
                time.sleep(60)
                continue

            for p in products:
                msg = f"""
🔥 {p['title']}

💰 Cost: ${p['cost']}
🏷 Sell: ${p['sell']}
📈 Profit: ${p['profit']}

🖼 {p['image']}
"""
                send_telegram(msg)

            time.sleep(300)

        except Exception as e:
            send_telegram(f"❌ Error: {str(e)}")
            time.sleep(60)


if __name__ == "__main__":
    run_bot()
