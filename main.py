import os
import time
import requests

from app.supplier_connector import fetch_cj_products
from app.listing_generator import generate_listing

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

LWA_CLIENT_ID = os.getenv("LWA_CLIENT_ID")
LWA_CLIENT_SECRET = os.getenv("LWA_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

SELLER_ID = os.getenv("SELLER_ID")
MARKETPLACE_ID = os.getenv("MARKETPLACE_ID")


def send_telegram(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram not configured")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    })


def get_amazon_access_token():
    url = "https://api.amazon.com/auth/o2/token"

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": LWA_CLIENT_ID,
        "client_secret": LWA_CLIENT_SECRET
    }

    response = requests.post(url, data=payload)
    data = response.json()

    print("Amazon token response:", data)

    return data.get("access_token")


def create_amazon_listing(product, listing, access_token):
    sku = f"cj-{int(time.time())}"

    url = f"https://sellingpartnerapi-eu.amazon.com/listings/2021-08-01/items/{SELLER_ID}/{sku}"

    headers = {
        "x-amz-access-token": access_token,
        "Content-Type": "application/json"
    }

    body = {
        "productType": listing["product_type"],
        "requirements": "LISTING",
        "attributes": {
            "item_name": [
                {
                    "value": listing["title"],
                    "marketplace_id": MARKETPLACE_ID
                }
            ],
            "brand": [
                {
                    "value": listing["brand"],
                    "marketplace_id": MARKETPLACE_ID
                }
            ],
            "description": [
                {
                    "value": listing["description"],
                    "marketplace_id": MARKETPLACE_ID
                }
            ],
            "bullet_point": [
                {
                    "value": bullet,
                    "marketplace_id": MARKETPLACE_ID
                }
                for bullet in listing["bullets"]
            ]
        }
    }

    if product.get("image"):
        body["attributes"]["main_product_image_locator"] = [
            {
                "media_location": product["image"],
                "marketplace_id": MARKETPLACE_ID
            }
        ]

    response = requests.put(url, headers=headers, json=body)

    print("Amazon listing response:", response.status_code)
    print(response.text)

    return response.status_code, response.text


def main():
    print("🚀 CJ → Amazon listing bot started")

    while True:
        try:
            products = fetch_cj_products()
            print(f"Found {len(products)} CJ products")

            access_token = get_amazon_access_token()

            if not access_token:
                send_telegram("❌ Amazon token failed")
                time.sleep(300)
                continue

            for product in products:
                listing = generate_listing(product)

                status, response_text = create_amazon_listing(
                    product,
                    listing,
                    access_token
                )

                message = f"""
📦 Amazon listing attempt

Product: {product['name']}
Price: ${listing['price']}
Profit: ${product.get('profit')}

Amazon status: {status}

Response:
{response_text[:1000]}
"""

                send_telegram(message)

                time.sleep(3)

        except Exception as e:
            print("ERROR:", e)
            send_telegram(f"❌ Bot error: {e}")

        print("⏳ Waiting 10 minutes")
        time.sleep(600)


if __name__ == "__main__":
    main()
