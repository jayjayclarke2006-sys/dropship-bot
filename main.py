import os
import time
import requests

from app.product_research import find_products


# =========================
# ENV VARIABLES
# =========================
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

LWA_CLIENT_ID = os.getenv("LWA_CLIENT_ID")
LWA_CLIENT_SECRET = os.getenv("LWA_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")


# =========================
# TELEGRAM
# =========================
def send_telegram_message(text):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text,
            "parse_mode": "HTML"
        }

        requests.post(url, json=payload)
    except Exception as e:
        print("❌ Telegram error:", e)


# =========================
# AMAZON TOKEN (SAFE)
# =========================
def get_amazon_access_token():
    try:
        url = "https://api.amazon.com/auth/o2/token"

        payload = {
            "grant_type": "refresh_token",
            "refresh_token": REFRESH_TOKEN,
            "client_id": LWA_CLIENT_ID,
            "client_secret": LWA_CLIENT_SECRET
        }

        response = requests.post(url, data=payload)
        data = response.json()

        print("Amazon response:", data)

        if "access_token" in data:
            return data["access_token"]
        else:
            raise Exception(data)

    except Exception as e:
        print("❌ Amazon token failed:", e)
        return None


# =========================
# FORMAT PRODUCT
# =========================
def format_product(product):
    return f"""
🔥 <b>{product.get('title', 'No title')}</b>

💰 Price: ${product.get('price', 'N/A')}
📈 Profit: ${product.get('profit', 'N/A')}
📊 Trend Score: {product.get('trend_score', 'N/A')}

🔗 {product.get('link', '')}
"""


# =========================
# MAIN BOT LOOP
# =========================
def main():
    print("🚀 Bot started...")

    while True:
        try:
            # 🔥 Try Amazon (but DON'T break bot if it fails)
            token = get_amazon_access_token()
            if token:
                print("✅ Amazon connected")
            else:
                print("⚠️ Amazon not connected (continuing)")

            # 🔍 Get products
            products = find_products()
            print(f"📦 Found {len(products)} products")

            # 📲 Send to Telegram
            for product in products:
                msg = format_product(product)
                send_telegram_message(msg)
                time.sleep(2)

        except Exception as e:
            print("🔥 MAIN LOOP ERROR:", e)

        # ⏳ Wait 5 minutes
        time.sleep(300)


# =========================
# RUN
# =========================
if __name__ == "__main__":
    print("🔥 FILE STARTED")
    main()
