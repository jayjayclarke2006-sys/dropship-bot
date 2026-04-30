import requests

CJ_API_KEY = "YOUR_CJ_API_KEY"  # put in env later


def fetch_cj_products():
    url = "https://developers.cjdropshipping.com/api2.0/v1/product/list"

    headers = {
        "CJ-Access-Token": CJ_API_KEY
    }

    params = {
        "pageNum": 1,
        "pageSize": 20
    }

    try:
        res = requests.get(url, headers=headers, params=params)
        data = res.json()

        products = []

        for item in data.get("data", {}).get("list", []):
            cost = float(item.get("sellPrice", 0))

            products.append({
                "name": item.get("productName"),
                "recommended_price": round(cost * 2.5, 2),
                "profit": round(cost * 1.5, 2),
                "trend_score": 80  # placeholder
            })

        return products

    except Exception as e:
        print("CJ API error:", e)
        return []
