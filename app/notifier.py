import os
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_alert(product):
    message = f"""
🔥 NEW PRODUCT FOUND 🔥

📦 {product['name']}
💰 Profit: ${product['profit']}
📊 Score: {product.get('score', 'N/A')}
⚠️ Risk: {product.get('risk', 'unknown')}

💵 Buy: ${product['supplier_price']}
🛒 Sell: ${product['amazon_price']}
"""

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })
