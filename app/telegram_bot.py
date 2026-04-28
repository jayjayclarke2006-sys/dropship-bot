import requests

TELEGRAM_TOKEN = "8700111978:AAHePxkgei_pvxoyTckQTkEaCf64GmnviH8"
CHAT_ID = "5717589829"


def send_telegram_message(text):
    print("🚀 Sending TEXT to Telegram...")

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    response = requests.post(url, data=data)

    print("📩 TEXT response:", response.text)


def send_telegram_photo(image_url, caption):
    print("🚀 Sending PHOTO to Telegram...")

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"

    data = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption
    }

    response = requests.post(url, data=data)

    print("📩 PHOTO response:", response.text)
