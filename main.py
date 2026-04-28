import os
import time
import requests
import random
from bs4 import BeautifulSoup

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

sent_products = set()

print("🚀 BOT STARTING...")


# ===== SEND PRODUCT =====
def send_product(product):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    msg = f"""🔥 {product['name']}

💰 Profit: ${product['profit']}
📊 Score: {product['score']}
⚠️ Risk: {product['risk']}

🛒 {product['link']}

🧠 {product['reason']}
"""

    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    res = requests.post(url, data=data)
    print("Telegram:", res.text)


# ===== REAL PRODUCT SCRAPER =====
def get_products():
    headers = {"User-Agent": "Mozilla/5.0"}

    keywords = [
        "tiktok gadgets",
        "amazon best sellers electronics",
        "cool tech gadgets",
        "smart home devices",
    ]

    url = f"https://www.amazon.com/s?k={random.choice(keywords).replace(' ', '+')}"
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.select(".s-result-item h2 a span")

    products = []

    for item in items:
        name = item.text.strip()

        if len(name) < 10 or name in sent_products:
            continue

        # ===== SIMULATED REAL PRICING =====
        selling_price = random.uniform(25, 80)
        cost_price = selling_price * random.uniform(0.3, 0.6)
        profit = round(selling_price - cost_price, 2)

        score = round((profit * 0.6) + random.uniform(10, 20), 2)

        # ===== SIMPLE TREND LOGIC =====
        if any(x in name.lower() for x in ["led", "smart", "mini", "portable"]):
            trend_boost = "🔥 Trending style product"
            score += 5
        else:
            trend_boost = "📦 General product"

        product = {
            "name": name,
            "profit": profit,
            "score": round(score, 2),
            "risk": "low" if profit > 20 else "medium",
            "link": f"https://www.amazon.com/s?k={name.replace(' ', '+')}",
            "reason": trend_boost
        }

        products.append(product)
        sent_products.add(name)

        if len(products) == 3:
            break

    return products


# ===== MAIN LOOP =====
def run_bot():
    while True:
        print("🔥 FINDING REAL PRODUCTS...")

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
