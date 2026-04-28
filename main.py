import os
import time
import requests
import random
from bs4 import BeautifulSoup

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("🚀 BOT STARTING...")


# ===== SEND PRODUCT =====
def send_product(product):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    msg = f"""🔥 {product['name']}

💰 Profit: ${product['profit']}
📊 Score: {product['score']}
⚠️ Risk: {product['risk']}

🛒 {product['link']}
"""

    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    res = requests.post(url, data=data)
    print("Telegram:", res.text)


# ===== SCRAPE AMAZON =====
def get_products():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    keywords = random.choice([
        "tiktok gadgets",
        "cool gadgets",
        "smart home devices",
        "fitness gadgets",
        "tech accessories"
    ])

    url = f"https://www.amazon.com/s?k={keywords.replace(' ', '+')}"
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    items = soup.select(".s-result-item h2 a span")

    products = []

    for item in items[:10]:
        name = item.text

        profit = round(random.uniform(15, 50), 2)
        score = round(random.uniform(25, 45), 2)

        products.append({
            "name": name,
            "profit": profit,
            "score": score,
            "risk": "low",
            "link": f"https://www.amazon.com/s?k={name.replace(' ', '+')}"
        })

    return random.sample(products, 3)


# ===== MAIN LOOP =====
def run_bot():
    while True:
        print("🔥 FETCHING REAL PRODUCTS...")

        try:
            products = get_products()

            for p in products:
                print("📤 Sending:", p["name"])
                send_product(p)

        except Exception as e:
            print("❌ ERROR:", e)

        print("⏳ Waiting 10 minutes...\n")
        time.sleep(600)


if __name__ == "__main__":
    run_bot()
