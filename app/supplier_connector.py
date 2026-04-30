import os
import requests

CJ_EMAIL = os.getenv("CJ_EMAIL")
CJ_PASSWORD = os.getenv("CJ_PASSWORD")

BASE_URL = "https://developers.cjdropshipping.com/api2.0/v1"


def get_access_token():
    url = f"{BASE_URL}/authentication/getAccessToken"

    payload = {
        "email": CJ_EMAIL,
        "password": CJ_PASSWORD
    }

    res = requests.post(url, json=payload)
    data = res.json()

    if data.get("result"):
        return data["data"]["accessToken"]
    else:
        print("CJ auth failed:", data)
        return None


def fetch_cj_products():
    token = get_access_token()
    if not token:
        return []

    url = f"{BASE_URL}/product/list"

    headers = {
        "CJ-Access-Token": token
    }

    res = requests.get(url, headers=headers)
    data = res.json()

    if not data.get("result"):
        print("CJ error:", data)
        return []

    products = []

    for item in data.get("data", [])[:3]:
        products.append({
            "name": item.get("productName"),
            "image": item.get("productImage"),
            "price": float(item.get("sellPrice", 10))
        })

    return products
