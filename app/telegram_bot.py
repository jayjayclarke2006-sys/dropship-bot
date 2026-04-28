import requests

# 🔐 PUT YOUR REAL VALUES HERE
TELEGRAM_TOKEN = "8700111978:AAFw0hdkSz8CCuTzECp_hMf_rLNbQVXfiVM"
CHAT_ID = "5717589892"


def send_telegram_message(text):
    print("🚀 Sending to Telegram...")

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }

    response = requests.post(url, data=data)

    print("📩 Telegram response:", response.text)
