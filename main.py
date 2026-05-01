import os
import requests
import time
import random

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})


# 🔥 Better keywords (high intent)
KEYWORDS = [
    "mini projector 1080p portable",
    "wireless earbuds bluetooth noise cancelling",
    "smart watch fitness tracker waterproof",
    "led strip lights room rgb",
    "gaming keyboard rgb mechanical",
    "portable blender usb rechargeable",
    "car phone holder magnetic mount",
    "laptop cooling pad fan rgb"
]


# 🧠 Generate better listing title
def generate_title(keyword):
    return f"{keyword.title()} – High Quality Trending Product"


# 🧾 Generate Amazon bullets
def generate_bullets(keyword):
    return [
        f"Premium {keyword} with modern design",
        "High performance and durable build",
        "Perfect for everyday use",
        "Trending product with high demand",
        "Limited stock opportunity"
    ]


# 🔍 Product engine
def get_products():
    products = []

    for k in KEYWORDS:
        cost = round(random.uniform(5, 30), 2)

        sell = round(cost * random.uniform(2.3, 2.8), 2)
        profit = round(sell - cost, 2)

        demand = random.randint(6, 10)
        competition = random.randint(3, 10)

        if profit > 15 and demand >= 7 and competition <= 7:
            decision = "✅ WIN"
        else:
            decision = "❌ SKIP"

        products.append({
            "keyword": k,
            "title": generate_title(k),
            "bullets": generate_bullets(k),
            "link": f"https://www.amazon.com/s?k={k.replace(' ', '+')}",
            "cost": cost,
            "sell": sell,
            "profit": profit,
            "demand": demand,
            "competition": competition,
            "decision": decision
        })

    return products


def run_bot():
    send_telegram("🚀 Bot running (LEVEL 4 MODE)")

    while True:
        try:
            products = get_products()

            for p in products:
                msg = f"""
🔥 {p['title']}

{p['decision']}

📈 Demand: {p['demand']}/10
⚔️ Competition: {p['competition']}/10

💰 Cost: ${p['cost']}
🏷 Your Price: ${p['sell']}
💸 Profit: ${p['profit']}

🧾 BULLETS:
- {p['bullets'][0]}
- {p['bullets'][1]}
- {p['bullets'][2]}
- {p['bullets'][3]}
- {p['bullets'][4]}

🔗 {p['link']}
"""
                send_telegram(msg)

            time.sleep(300)

        except Exception as e:
            send_telegram(f"❌ Error: {str(e)}")
            time.sleep(60)


if __name__ == "__main__":
    run_bot()
