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
        print("Auth failed:", data)
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
        print("CJ API error:", data)
        return []

    products = []

    for item in data.get("data", [])[:5]:
        products.append({
            "name": item.get("productName"),
            "price": float(item.get("sellPrice", 10)),
            "sales": item.get("sales", 0),
            "link": item.get("productUrl")
        })

    return products
