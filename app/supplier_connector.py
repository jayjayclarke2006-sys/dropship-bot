import os
import requests

CJ_EMAIL = os.getenv("CJ_EMAIL")
CJ_PASSWORD = os.getenv("CJ_PASSWORD")

BASE_URL = "https://developers.cjdropshipping.com/api2.0/v1"


def get_cj_token():
    try:
        url = f"{BASE_URL}/authentication/getAccessToken"

        payload = {
            "email": CJ_EMAIL,
            "password": CJ_PASSWORD
        }

        r = requests.post(url, json=payload, timeout=30)
        data = r.json()

        print("CJ AUTH:", data)

        if data.get("result") and data.get("data"):
            return data["data"].get("accessToken")

    except Exception as e:
        print("CJ TOKEN ERROR:", e)

    return None


def fetch_cj_products():
    try:
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
            "pageSize": 5,
            "productNameEn": "phone"   # 🔥 forces results
        }

        r = requests.get(url, headers=headers, params=params, timeout=30)
        data = r.json()

        print("CJ PRODUCTS RAW:", data)

        if not data.get("result"):
            return []

        items = data.get("data", {}).get("list", [])

        products = []

        for item in items:
            name = item.get("productNameEn") or item.get("productName") or "CJ Product"

            supplier_price = item.get("sellPrice") or item.get("price") or 10

            try:
                supplier_price = float(supplier_price)
            except:
                supplier_price = 10

            selling_price = round(supplier_price * 2.5, 2)
            profit = round(selling_price - supplier_price, 2)

            image = item.get("productImage") or ""
            link = item.get("productUrl") or ""

            products.append({
                "title": name,
                "price": selling_price,
                "profit": profit,
                "trend_score": round(profit / max(supplier_price, 1), 2),
                "image": image,
                "link": link
            })

        return products

    except Exception as e:
        print("CJ FETCH ERROR:", e)
        return []
