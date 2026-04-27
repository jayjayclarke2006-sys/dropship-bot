import os
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("DEBUG TOKEN:", TELEGRAM_TOKEN)
print("DEBUG CHAT:", CHAT_ID)


def send_telegram_message(text):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("❌ Telegram not configured")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, data=data)
    print("📤 Telegram response:", response.text)


def send_telegram_photo(image_url, caption):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("❌ Telegram not configured")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"

    data = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, data=data)
    print("📤 Photo response:", response.text)
