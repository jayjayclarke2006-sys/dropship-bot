import os
import time
import requests

# ========================
# ENV VARIABLES
# ========================
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

LWA_CLIENT_ID = os.getenv("LWA_CLIENT_ID")
LWA_CLIENT_SECRET = os.getenv("LWA_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

SELLER_ID = os.getenv("SELLER_ID")
MARKETPLACE_ID = os.getenv("MARKETPLACE_ID")


# ========================
# GET AMAZON ACCESS TOKEN
# ========================
def get_access_token():
    url = "https://api.amazon.com/auth/o2/token"

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": LWA_CLIENT_ID,
        "client_secret": LWA_CLIENT_SECRET
    }

    res = requests.post(url, data=payload)
    data = res.json()

    print("Access token response:", data)

    return data.get("access_token")


# ========================
# CREATE AMAZON LISTING
# ========================
def create_listing(product, access_token):
    sku = f"sku-{int(time.time())}"

    url = f"https://sellingpartnerapi-eu.amazon.com/listings/2021-08-01/items/{SELLER_ID}/{sku}"

    headers = {
        "x-amz-access-token": access_token,
        "Content-Type": "application/json"
    }

    body = {
        "productType": "PRODUCT",
        "requirements": "LISTING",
        "attributes": {
            "item_name": [{"value": product["name"]}],
            "brand": [{"value": "Generic"}],
            "description": [{"value": product["name"]}],
            "bullet_point": [
                {"value": "High demand product"},
                {"value": "Fast shipping"},
                {"value": "Great value"}
            ]
        },
        "offers": [
            {
                "marketplaceId": MARKETPLACE_ID,
                "price": {
                    "currency": "GBP",
                    "amount": "9.99"
                }
            }
        ]
    }

    res = requests.put(url, headers=headers, json=body)

    print("Listing response:", res.status_code)
    print(res.text)

    return res.text


# ========================
# TEST PRODUCT
# ========================
def get_test_product():
    return {
        "name": "Wireless Earbuds"
    }


# ========================
# TELEGRAM
# ========================
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": msg
    })


# ========================
# MAIN LOOP
# ========================
def main():
    print("🚀 Bot started...")

    while True:
        try:
            product = get_test_product()

            token = get_access_token()

            if not token:
                print("❌ Failed to get token")
                continue

            response = create_listing(product, token)

            send_telegram(f"📦 Sent to Amazon: {product['name']}")

        except Exception as e:
            print("❌ ERROR:", e)

        time.sleep(300)  # every 5 mins


if __name__ == "__main__":
    main()
