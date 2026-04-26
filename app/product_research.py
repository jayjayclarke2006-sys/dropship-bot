import random

# -------------------------------
# STEP 1: Supplier Products
# -------------------------------
def get_supplier_products():
    return [
        {"name": "Wireless Earbuds", "supplier_price": random.randint(8, 15), "niche": "electronics"},
        {"name": "Phone Holder", "supplier_price": random.randint(2, 6), "niche": "accessories"},
        {"name": "LED Strip Lights", "supplier_price": random.randint(5, 10), "niche": "home"},
        {"name": "Bluetooth Speaker", "supplier_price": random.randint(10, 20), "niche": "electronics"},
        {"name": "Fitness Resistance Bands", "supplier_price": random.randint(4, 9), "niche": "fitness"},
        {"name": "Mini Projector", "supplier_price": random.randint(25, 40), "niche": "electronics"},
    ]

# -------------------------------
# STEP 2: Amazon Price Simulation
# -------------------------------
amazon_prices = {
    "Wireless Earbuds": 29.99,
    "Phone Holder": 14.99,
    "LED Strip Lights": 25.99,
    "Bluetooth Speaker": 39.99,
    "Fitness Resistance Bands": 19.99,
    "Mini Projector": 79.99,
}

# -------------------------------
# STEP 3: Trend + Demand Engine
# -------------------------------
def get_trend_score(niche):
    trending_niches = {
        "electronics": random.randint(6, 10),
        "fitness": random.randint(5, 9),
        "home": random.randint(4, 8),
        "accessories": random.randint(3, 7),
    }
    return trending_niches.get(niche, 5)

# -------------------------------
# STEP 4: Product Scoring System
# -------------------------------
def score_product(product, trend_score):
    score = 0

    # Profit scoring
    if product["profit"] > 20:
        score += 4
    elif product["profit"] > 10:
        score += 3
    elif product["profit"] > 5:
        score += 1

    # Price sweet spot
    if 10 < product["amazon_price"] < 80:
        score += 2

    # Trend score
    if trend_score > 7:
        score += 3
    elif trend_score > 5:
        score += 2

    # Random demand simulation
    demand = random.randint(1, 10)
    if demand > 7:
        score += 2

    return score

# -------------------------------
# STEP 5: Main Product Finder
# -------------------------------
def find_products():
    supplier_products = get_supplier_products()
    profitable = []

    for p in supplier_products:
        name = p["name"]
        supplier_price = p["supplier_price"]
        niche = p["niche"]

        amazon_price = amazon_prices.get(name)
        if not amazon_price:
            continue

        profit = amazon_price - supplier_price
        trend_score = get_trend_score(niche)

        product_data = {
            "name": name,
            "supplier_price": supplier_price,
            "amazon_price": amazon_price,
            "profit": round(profit, 2),
            "niche": niche,
            "trend_score": trend_score
        }

        score = score_product(product_data, trend_score)

        if score >= 6:
            product_data["score"] = score
            profitable.append(product_data)

    return profitable
