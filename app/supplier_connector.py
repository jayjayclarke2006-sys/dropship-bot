import os
import requests

CJ_EMAIL = os.getenv("CJ_EMAIL")
CJ_PASSWORD = os.getenv("CJ_PASSWORD")

BASE_URL = "https://developers.cjdropshipping.com/api2.0/v1"


def get_cj_token():
    url = f"{BASE_URL}/authentication/getAccessToken"
    payload = {
        "email": CJ_EMAIL,
        "password": CJ_PASSWORD
    }

    r = requests.post(url, json=payload, timeout=30)
    data = r.json()
    print("CJ auth response:", data)

    if data.get("result") and data.get("data"):
        return data["data"].get("accessToken")

    return None


def fetch_cj_products():
    token = get_cj_token()
    if not token:
        print("No CJ token")
        return []

    url = f"{BASE_URL}/product/list"

    headers = {
        "CJ-Access-Token": token
    }

    params = {
        "pageNum": 1,
        "pageSize": 5
    }

    r = requests.get(url, headers=headers, params=params, timeout=30)
    data = r.json()
    print("CJ product response:", data)

    if not data.get("result"):
        return []

    raw_data = data.get("data", {})
    items = raw_data.get("list", raw_data if isinstance(raw_data, list) else [])

    products = []

    for item in items:
        name = item.get("productName") or item.get("name") or "CJ Product"

        supplier_price = (
            item.get("sellPrice")
            or item.get("price")
            or item.get("productSellPrice")
            or 9.99
        )

        try:
            supplier_price = float(supplier_price)
        except:
            supplier_price = 9.99

        selling_price = round(supplier_price * 2.5, 2)
        profit = round(selling_price - supplier_price, 2)

        image = (
            item.get("productImage")
            or item.get("image")
            or item.get("productImageSet")
            or ""
        )

        if isinstance(image, list) and image:
            image = image[0]

        products.append({
            "title": name,
            "name": name,
            "price": selling_price,
            "supplier_price": supplier_price,
            "profit": profit,
            "trend_score": round(profit / max(supplier_price, 1), 2),
            "image": image,
            "link": item.get("productUrl") or item.get("sourceFrom") or "",
            "niche": "general"
        })

    return products
