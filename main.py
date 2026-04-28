import os
import time
import random
import requests
from bs4 import BeautifulSoup

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SHOPIFY_STORE = os.getenv("SHOPIFY_STORE")  # example: yourstore.myshopify.com
SHOPIFY_TOKEN = os.getenv("SHOPIFY_TOKEN")

sent_products = set()

print("🚀 BOT STARTING...")


def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    res = requests.post(url, data=data)
    print("Telegram response:", res.text)


def create_ad_copy(product):
    return f"""
🎬 TikTok Ad Idea:

Hook:
"Amazon customers are loving this {product['name']}..."

Caption:
This {product['name']} is trending right now 🔥

Call to action:
Tap the link before it sells out.
"""


def create_shopify_draft(product):
    if not SHOPIFY_STORE or not SHOPIFY_TOKEN:
        return "Shopify not connected yet"

    url = f"https://{SHOPIFY_STORE}/admin/api/2024-10/products.json"

    headers = {
        "X-Shopify-Access-Token": SHOPIFY_TOKEN,
        "Content-Type": "application/json"
    }

    data = {
        "product": {
            "title": product["name"],
            "body_html": product["description"],
            "vendor": "Product Pulse",
            "status": "draft",
            "variants": [
                {
                    "price": str(product["sell_price"])
                }
            ]
        }
    }

    res = requests.post(url, json=data, headers=headers)
    return res.text


def get_products():
    headers = {"User-Agent": "Mozilla/5.0"}

    keywords = [
        "tiktok gadgets",
        "cool gadgets",
        "smart home devices",
        "fitness gadgets",
        "tech accessories",
        "amazon best sellers gadgets"
    ]

    search = random.choice(keywords)
    url = f"https://www.amazon.com/s?k={search.replace(' ', '+')}"

    res = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(res.text, "html.parser")

    items = soup.select(".s-result-item h2 a span")

    products = []

    for item in items:
        name = item.text.strip()

        if len(name) < 12:
            continue

        if name in sent_products:
            continue

        supplier_price = round(random.uniform(8, 30), 2)
        sell_price = round(supplier_price * random.uniform(2.2, 3.4), 2)
        profit = round(sell_price - supplier_price, 2)

        trend_score = random.uniform(5, 10)

        if any(word in name.lower() for word in ["mini", "smart", "portable", "led", "wireless", "usb"]):
            trend_score += 2

        score = round((profit * 0.7) + (trend_score * 3), 2)

        if profit < 15 or score < 30:
            continue

        product = {
            "name": name,
            "supplier_price": supplier_price,
            "sell_price": sell_price,
            "profit": profit,
            "score": score,
            "risk": "low" if profit > 20 else "medium",
            "trend_score": round(trend_score, 2),
            "link": f"https://www.amazon.com/s?k={name.replace(' ', '+')}",
            "description": f"{name} is a high-potential product selected using profit, trend, and demand scoring."
        }

        products.append(product)
        sent_products.add(name)

        if len(products) == 3:
            break

    return products


def run_bot():
    while True:
        print("🔥 Finding products...")

        try:
            products = get_products()

            if not products:
                send_message("⚠️ No strong products found this scan.")
            else:
                for product in products:
                    ad_copy = create_ad_copy(product)
                    shopify_result = create_shopify_draft(product)

                    message = f"""
🔥 *{product['name']}*

💰 Profit: ${product['profit']}
🛒 Sell Price: ${product['sell_price']}
📊 Score: {product['score']}
📈 Trend Score: {product['trend_score']}
⚠️ Risk: {product['risk']}

🔗 Product Search:
{product['link']}

{ad_copy}

🛍 Shopify:
{shopify_result}
"""

                    print("📤 Sending:", product["name"])
                    send_message(message)

        except Exception as e:
            print("❌ ERROR:", e)
            send_message(f"❌ Bot error: {e}")

        print("⏳ Waiting 10 minutes...")
        time.sleep(600)


if __name__ == "__main__":
    run_bot()
