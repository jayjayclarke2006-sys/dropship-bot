import requests

TELEGRAM_TOKEN = "8700111978:AAGTViZz3ie8zTpj_mV1AOe296BqIWyEvoY"
CHAT_ID = "5717589829"


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
