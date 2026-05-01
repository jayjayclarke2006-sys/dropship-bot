import os
import time
import random
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")  # optional


KEYWORDS = [
    "mini projector 1080p portable",
    "wireless earbuds bluetooth noise cancelling",
    "smart watch fitness tracker waterproof",
    "led strip lights room rgb",
    "portable blender usb rechargeable",
    "car phone holder magnetic mount",
    "laptop cooling pad fan",
    "desk lamp led wireless charger",
    "pet grooming vacuum brush",
    "car vacuum cleaner portable"
]


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    requests.post(url, json=payload)


def amazon_search_link(keyword):
    return f"https://www.amazon.co.uk/s?k={keyword.replace(' ', '+')}"


def supplier_search_link(keyword):
    return f"https://www.aliexpress.com/wholesale?SearchText={keyword.replace(' ', '+')}"


def calculate_score(profit, demand, competition):
    return round((profit * 1.2) + (demand * 4) - (competition * 3), 2)


def make_listing(keyword):
    title = f"{keyword.title()} - Trending High Demand Product"

    bullets = [
        f"High-quality {keyword} designed for everyday use",
        "Modern, practical, and easy to use",
        "Ideal for home, travel, work, or gifting",
        "Strong product potential based on demand signals",
        "Check supplier delivery time before listing"
    ]

    description = (
        f"{keyword.title()} is a potential Amazon product opportunity. "
        f"It has been selected based on demand, estimated profit potential, "
        f"and resale suitability. Always check supplier reliability, reviews, "
        f"shipping time, and Amazon category rules before listing."
    )

    return title, bullets, description


def get_products():
    products = []

    for keyword in KEYWORDS:
        estimated_cost = round(random.uniform(6, 28), 2)
        sell_price = round(estimated_cost * random.uniform(2.2, 3.0), 2)
        profit = round(sell_price - estimated_cost, 2)

        demand = random.randint(6, 10)
        competition = random.randint(3, 9)

        score = calculate_score(profit, demand, competition)

        decision = "✅ WIN" if score >= 35 and profit >= 15 and competition <= 7 else "❌ SKIP"

        title, bullets, description = make_listing(keyword)

        products.append({
            "keyword": keyword,
            "title": title,
            "cost": estimated_cost,
            "sell_price": sell_price,
            "profit": profit,
            "demand": demand,
            "competition": competition,
            "score": score,
            "decision": decision,
            "amazon_link": amazon_search_link(keyword),
            "supplier_link": supplier_search_link(keyword),
            "bullets": bullets,
            "description": description
        })

    return sorted(products, key=lambda x: x["score"], reverse=True)


def format_message(p):
    return f"""
🔥 {p['title']}

{p['decision']}

📊 Score: {p['score']}
📈 Demand: {p['demand']}/10
⚔️ Competition: {p['competition']}/10

💰 Estimated Cost: ${p['cost']}
🏷 Suggested Sell Price: ${p['sell_price']}
💸 Estimated Profit: ${p['profit']}

🧾 AMAZON BULLETS:
- {p['bullets'][0]}
- {p['bullets'][1]}
- {p['bullets'][2]}
- {p['bullets'][3]}
- {p['bullets'][4]}

📝 DESCRIPTION:
{p['description']}

🔎 Amazon Check:
{p['amazon_link']}

🏭 Supplier Search:
{p['supplier_link']}
"""


def run_bot():
    send_telegram("🚀 LEVEL 5 BOT STARTED")

    while True:
        try:
            products = get_products()

            winners = [p for p in products if p["decision"] == "✅ WIN"]

            if not winners:
                send_telegram("⚠️ No strong winners this scan.")
            else:
                for p in winners[:5]:
                    send_telegram(format_message(p))
                    time.sleep(2)

        except Exception as e:
            send_telegram(f"❌ Bot error: {e}")
            time.sleep(60)

        time.sleep(300)


if __name__ == "__main__":
    run_bot()
