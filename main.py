import time
import requests
import random

# ===== CONFIG =====
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

DELAY = 5400  # 1.5 hours


# ===== TELEGRAM FUNCTION =====
def send(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})


# ===== PRODUCTS (EDIT LATER IF YOU WANT) =====
def get_products():
    return [
        {
            "name": "Portable Blender USB Rechargeable",
            "cost": 5.50,
            "image": "https://m.media-amazon.com/images/I/61example.jpg",
            "keyword": "portable blender"
        },
        {
            "name": "LED Strip Lights RGB",
            "cost": 6.20,
            "image": "https://m.media-amazon.com/images/I/62example.jpg",
            "keyword": "led strip lights"
        },
        {
            "name": "Gaming Keyboard RGB",
            "cost": 12.00,
            "image": "https://m.media-amazon.com/images/I/63example.jpg",
            "keyword": "gaming keyboard"
        }
    ]


# ===== GENERATE LISTING =====
def make_listing(p):
    sell = round(p["cost"] * 3, 2)
    profit = round(sell - p["cost"], 2)

    description = f"""
This {p['name']} is designed for everyday convenience. It is lightweight, easy to use, and perfect for home, travel, or office use.

Built with durable materials, it provides reliable performance and is simple to clean and maintain.
"""

    bullets = [
        "Portable and lightweight design",
        "Easy to use and clean",
        "Durable build quality",
        "Suitable for home or travel",
        "Reliable everyday performance"
    ]

    return sell, profit, description.strip(), bullets


# ===== MAIN LOOP =====
def run():
    send("✅ Bot started")

    while True:
        try:
            products = random.sample(get_products(), 2)

            for p in products:
                sell, profit, desc, bullets = make_listing(p)

                msg = f"""
🔥 {p['name']}

💰 Cost: ${p['cost']}
🏷 Sell: ${sell}
📈 Profit: ${profit}

📝 DESCRIPTION:
{desc}

📌 BULLETS:
- {bullets[0]}
- {bullets[1]}
- {bullets[2]}
- {bullets[3]}
- {bullets[4]}

🖼 IMAGE:
{p['image']}

🔍 SEARCH:
https://www.amazon.co.uk/s?k={p['keyword'].replace(" ", "+")}
"""

                send(msg)
                time.sleep(5)

        except Exception as e:
            send(f"❌ Error: {e}")

        time.sleep(DELAY)


# ===== START =====
run()
