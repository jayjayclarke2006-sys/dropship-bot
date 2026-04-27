from app.supplier import get_supplier_products
import random

# -------------------------------
# Price Estimation
# -------------------------------
def estimate_amazon_price(supplier_price):
    return round(supplier_price * random.uniform(2.5, 4.5), 2)

# -------------------------------
# Trend Engine
# -------------------------------
def get_trend_score(niche):
    return random.randint(4, 10)

# -------------------------------
# Improved Scoring System
# -------------------------------
def score_product(product, trend_score):
    score = 0

    # Profit strength
    if product["profit"] > 25:
        score += 5
    elif product["profit"] > 15:
        score += 3
    elif product["profit"] > 10:
        score += 2

    # Sweet price range (conversion zone)
    if 15 < product["amazon_price"] < 80:
        score += 3

    # Trend strength
    if trend_score > 8:
        score += 4
    elif trend_score > 6:
        score += 2

    # Demand simulation
    demand = random.randint(1, 10)
    if demand > 7:
        score += 3

    return score

# -------------------------------
# Main Product Finder
# -------------------------------
def find_products():
    supplier_products = get_supplier_products()
    winners = []

    for p in supplier_products:
        supplier_price = p["supplier_price"]
        amazon_price = estimate_amazon_price(supplier_price)
        profit = amazon_price - supplier_price
        niche = p.get("niche", "general")

        trend_score = get_trend_score(niche)

        product_data = {
            "name": p["name"],
            "supplier_price": supplier_price,
            "amazon_price": amazon_price,
            "profit": round(profit, 2),
            "niche": niche,
            "trend_score": trend_score
        }

        score = score_product(product_data, trend_score)

        if score >= 6:
            product_data["score"] = score
            winners.append(product_data)

    return winners
