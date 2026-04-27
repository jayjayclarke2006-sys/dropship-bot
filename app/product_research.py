import random
from app.supplier import get_supplier_products

# 🔥 Simulated trend + demand engine
def get_trend_score(product_name):
    trending_keywords = ["wireless", "led", "bluetooth", "smart", "portable"]
    score = 5

    for keyword in trending_keywords:
        if keyword in product_name.lower():
            score += 2

    return min(score + random.uniform(0, 3), 10)


# 🔥 Assign niche automatically
def detect_niche(product_name):
    name = product_name.lower()

    if "led" in name:
        return "home decor"
    elif "wireless" in name or "bluetooth" in name:
        return "gadgets"
    elif "holder" in name:
        return "car accessories"
    else:
        return "general"


# 🔥 Main product finder
def find_products():
    supplier_products = get_supplier_products()

    # Simulated Amazon pricing
    amazon_prices = {
        "Wireless Earbuds": 29.99,
        "Phone Holder": 14.99,
        "LED Strip Lights": 25.99,
        "Bluetooth Speaker": 39.99
    }

    scored_products = []

    for p in supplier_products:
        name = p["name"]
        supplier_price = p["supplier_price"]
        amazon_price = amazon_prices.get(name, supplier_price * 2)

        profit = amazon_price - supplier_price
        trend_score = get_trend_score(name)
        niche = detect_niche(name)

        # 🔥 overall score formula
        score = (profit * 0.5) + (trend_score * 2)

        scored_products.append({
            "name": name,
            "supplier_price": supplier_price,
            "amazon_price": amazon_price,
            "profit": round(profit, 2),
            "trend_score": round(trend_score, 2),
            "score": round(score, 2),
            "niche": niche
        })

    # 🔥 sort best → worst
    scored_products.sort(key=lambda x: x["score"], reverse=True)

    # 🔥 pick best product
    best_product = scored_products[0] if scored_products else None

    return {
        "best_product": best_product,
        "all_products": scored_products
    }
