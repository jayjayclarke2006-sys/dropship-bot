import random


def find_products():
    products = [
        {"name": "Mini Projector", "supplier_price": 25, "niche": "tech"},
        {"name": "Smart Watch", "supplier_price": 30, "niche": "tech"},
        {"name": "Wireless Earbuds", "supplier_price": 15, "niche": "tech"},
        {"name": "LED Strip Lights", "supplier_price": 10, "niche": "home"},
        {"name": "Gaming Mouse", "supplier_price": 12, "niche": "gaming"},
    ]

    results = []

    for p in products:
        amazon_price = p["supplier_price"] * random.uniform(2.5, 3.5)
        profit = amazon_price - p["supplier_price"]

        trend_score = random.uniform(5, 10)
        score = profit + trend_score * 2

        risk = "low" if profit > 20 else "medium"

        link = f"https://www.amazon.com/s?k={p['name'].replace(' ', '+')}"

        results.append({
            "name": p["name"],
            "supplier_price": p["supplier_price"],
            "amazon_price": round(amazon_price, 2),
            "profit": round(profit, 2),
            "trend_score": round(trend_score, 2),
            "score": round(score, 2),
            "niche": p["niche"],
            "risk": risk,
            "link": link
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)
