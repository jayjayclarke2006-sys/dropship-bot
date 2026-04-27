import random
from app.supplier import get_supplier_products

def get_amazon_price(product_name):
    base_prices = {
        "Wireless Earbuds": 29.99,
        "Phone Holder": 14.99,
        "LED Strip Lights": 25.99,
        "Bluetooth Speaker": 39.99,
        "Mini Projector": 79.99,
        "Car Vacuum Cleaner": 34.99,
        "Smart Watch": 49.99,
        "Gaming Mouse": 19.99
    }
    return base_prices.get(product_name, random.uniform(15, 60))


def calculate_trend_score(niche):
    trends = {
        "tech": random.uniform(6, 10),
        "car": random.uniform(5, 9),
        "home": random.uniform(4, 8),
        "gaming": random.uniform(6, 9)
    }
    return trends.get(niche, random.uniform(3, 7))


def calculate_score(profit, trend_score):
    return round((profit * 0.6) + (trend_score * 2), 2)


def find_products():
    supplier_products = get_supplier_products()
    results = []

    for p in supplier_products:
        amazon_price = get_amazon_price(p["name"])
        profit = amazon_price - p["supplier_price"]

        # 🔥 FILTER (VERY IMPORTANT)
        if p["supplier_price"] > 50:
            continue

        if amazon_price < 15:
            continue

        if profit < 8:
            continue

        trend_score = calculate_trend_score(p["niche"])
        score = calculate_score(profit, trend_score)

        risk = "low" if profit > 15 else "medium"

        results.append({
            "name": p["name"],
            "supplier_price": p["supplier_price"],
            "amazon_price": round(amazon_price, 2),
            "profit": round(profit, 2),
            "trend_score": round(trend_score, 2),
            "score": score,
            "niche": p["niche"],
            "risk": risk,
            "image": f"https://source.unsplash.com/600x400/?{p['name'].replace(' ', '%20')}"
})

    return sorted(results, key=lambda x: x["score"], reverse=True)
