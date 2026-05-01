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


def send_telegram_message(text):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text,
            "parse_mode": "HTML"
        }

        r = requests.post(url, json=payload, timeout=30)
        print("Telegram response:", r.text)

    except Exception as e:
        print("Telegram error:", e)


def get_amazon_access_token():
    try:
        url = "https://api.amazon.com/auth/o2/token"

        payload = {
            "grant_type": "refresh_token",
            "refresh_token": REFRESH_TOKEN,
            "client_id": LWA_CLIENT_ID,
            "client_secret": LWA_CLIENT_SECRET
        }

        r = requests.post(url, data=payload, timeout=30)
        data = r.json()

        print("Amazon token response:", data)

        return data.get("access_token")

    except Exception as e:
        print("Amazon token error:", e)
        return None


def create_amazon_listing(product, listing, access_token):
    try:
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

        r = requests.put(url, headers=headers, json=body, timeout=30)

        print("Amazon listing status:", r.status_code)
        print("Amazon listing response:", r.text)

        return r.status_code, r.text

    except Exception as e:
        print("Amazon listing error:", e)
        return 500, str(e)


def format_telegram(product, listing, amazon_status=None):
    return f"""
🔥 <b>{listing['title']}</b>

💰 Price: ${listing.get('price', 'N/A')}
📈 Profit: ${listing.get('profit', 'N/A')}
📊 Trend Score: {product.get('trend_score', 'N/A')}

🖼 Image: {product.get('image', 'N/A')}
🔗 Supplier: {product.get('link', 'N/A')}

Amazon Status: {amazon_status if amazon_status else 'Not sent yet'}
"""


def main():
    print("🔥 FILE STARTED")
    print("🚀 CJ → Amazon bot started")

    while True:
        try:
            products = fetch_cj_products()
            print(f"Found {len(products)} CJ products")

            amazon_token = get_amazon_access_token()

            for product in products:
                listing = generate_listing(product)

                amazon_status = "Amazon token failed"

                if amazon_token:
                    status, response = create_amazon_listing(
                        product,
                        listing,
                        amazon_token
                    )
                    amazon_status = f"{status}: {response[:300]}"

                msg = format_telegram(product, listing, amazon_status)
                send_telegram_message(msg)

                time.sleep(3)

        except Exception as e:
            print("MAIN ERROR:", e)
            send_telegram_message(f"❌ Bot error: {e}")

        print("Sleeping 10 minutes")
        time.sleep(600)


if __name__ == "__main__":
    main()
