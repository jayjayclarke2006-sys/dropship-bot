import requests
import os


def get_config():
    return (
        os.getenv("TELEGRAM_BOT_TOKEN"),
        os.getenv("TELEGRAM_CHAT_ID")
    )


def send_telegram_message(text):
    BOT_TOKEN, CHAT_ID = get_config()

    if not BOT_TOKEN or not CHAT_ID:
        print("⚠️ Telegram not configured")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    requests.post(url, json=payload)


def send_telegram_photo(image_url, caption):
    BOT_TOKEN, CHAT_ID = get_config()

    if not BOT_TOKEN or not CHAT_ID:
        print("⚠️ Telegram not configured")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    payload = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption,
        "parse_mode": "HTML"
    }

    requests.post(url, json=payload)
