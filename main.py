import os
import time
import requests

# ====== TELEGRAM CONFIG ======
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("🚀 BOT STARTING...")
print("TOKEN:", TOKEN)
print("CHAT:", CHAT_ID)


# ====== SEND MESSAGE ======
def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    try:
        res = requests.post(url, data=data)
        print("Telegram response:", res.text)
    except Exception as e:
        print("❌ Error sending message:", e)


# ====== MAIN LOOP ======
def run_bot():
    while True:
        print("🔥 SCANNING PRODUCTS...")

        # Fake products (your working version)
        products = [
            {"name": "Mini Projector", "profit": 44.99, "score": 40.0, "risk": "low"},
            {"name": "Smart Watch", "profit": 33.99, "score": 39.2, "risk": "low"},
            {"name": "Wireless Earbuds", "profit": 21.99, "score": 28.0, "risk": "low"},
        ]

        print("🔥 TOP 3 PRODUCTS FOUND")

        for p in products:
            msg = f"""🔥 {p['name']}

💰 Profit: ${p['profit']}
📊 Score: {p['score']}
⚠️ Risk: {p['risk']}
"""

            print(f"📤 Sending {p['name']}...")
            send_message(msg)

        print("⏳ Waiting 10 minutes...\n")
        time.sleep(600)


# ====== START ======
if __name__ == "__main__":
    run_bot()
