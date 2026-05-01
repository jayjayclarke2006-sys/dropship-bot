import os
import requests
import time
import random

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})


# 🔍 Fetch REAL products (no login needed)
def fetch_products():
    url = "https://cjdropshipping.com/api2.0/v1/product/list"

    params = {
        "pageNum": 1,
        "pageSize": 10,
        "productName": random.choice([
            "projector",
            "earbuds",
            "smart watch",
            "led light",
            "keyboard",
            "gaming mouse"
        ])
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()

        if data.get("code") != 200:
            return []

        return data.get("data", {}).get("list", [])

    except:
        return []


# 🧠 Clean title
def clean_title(title):
    if not title:
        return "Trending Product"
    return title.replace("&amp;", "&")[:80]


# 💰 Pricing logic
def calculate_price(cost):
    sell = round(cost * 2.2, 2)
    profit = round(sell - cost, 2)
    return sell, profit


# 🧾 Generate bullets (FOR AMAZON LISTING)
def generate_bullets(title):
    return [
        f"High-quality {title.lower()} built for daily use",
        "Durable design with modern features",
        "Lightweight and easy to use",
        "Perfect for home, travel, or gifting",
        "Limited-time trending product"
    ]


# 🗂 Category suggestion
def get_category(title):
    t = title.lower()

    if "projector" in t:
        return "Electronics > Projectors"
    if "earbuds" in t or "headphone" in t:
        return "Electronics > Audio"
    if "watch" in t:
        return "Electronics > Wearables"
    if "light" in t:
        return "Home & Kitchen > Lighting"

    return "Home & Kitchen"


# 🧱 Build product object
def build_product(p):
    title = clean_title(p.get("productNameEn"))

    try:
        cost = float(p.get("sellPrice", 5))
    except:
        cost = 5.0

    sell, profit = calculate_price(cost)

    image = ""
    if p.get("productImage"):
        image = p["productImage"].split(",")[0]

    bullets = generate_bullets(title)
    category = get_category(title)

    return {
        "title": title,
        "cost": cost,
        "sell": sell,
        "profit": profit,
        "image": image,
        "bullets": bullets,
        "category": category
    }


def run_bot():
    send_telegram("✅ Bot started (UPGRADED MODE)")

    while True:
        try:
            products = fetch_products()

            if not products:
                send_telegram("❌ No products found (retrying...)")
                time.sleep(60)
                continue

            for p in products[:5]:
                item = build_product(p)

                msg = f"""
🔥 {item['title']}

💰 Cost: ${item['cost']}
🏷 Sell: ${item['sell']}
📈 Profit: ${item['profit']}

🗂 Category: {item['category']}

🧾 Bullets:
- {item['bullets'][0]}
- {item['bullets'][1]}
- {item['bullets'][2]}
- {item['bullets'][3]}
- {item['bullets'][4]}

🖼 {item['image']}
"""

                send_telegram(msg)

            time.sleep(300)

        except Exception as e:
            send_telegram(f"❌ Error: {str(e)}")
            time.sleep(60)


if __name__ == "__main__":
    run_bot()
