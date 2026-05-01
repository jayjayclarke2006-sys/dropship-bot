import time
import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }

    r = requests.post(url, json=payload)
    print("Telegram:", r.text)


def main():
    print("🚀 BOT STARTED")

    while True:
        print("LOOP RUNNING")
        send_telegram_message("✅ Bot is alive")
        time.sleep(60)


if __name__ == "__main__":
    main()
