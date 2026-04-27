from app.supplier import get_supplier_products
from app.pricing import calculate_price, analyze_risk
import random

# -------------------------------
# Trend Engine
# -------------------------------
def get_trend_score(niche):
    return random.randint(4, 10)

# -------------------------------
# Scoring System
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

    # Price range
    if 15 < product["amazon_price"] < 100:
        score += 3

    # Trend
    if trend_score > 8:
        score += 4
    elif trend_score > 6:
        score += 2

    # Competition
    if product["competition"] == "low":
        score += 4
    elif product["competition"] == "medium":
        score += 2

    # Reviews (lower = better opportunity)
    if product["reviews"] < 500:
        score += 3

    # Risk penalty
    if product["risk"] == "high":
        score -= 3

    return score

# -------------------------------
# Main Function
# -------------------------------
def find_products():
    supplier_products = get_supplier_products()
    winners = []

    for p in supplier_products:
        supplier_price = p["supplier_price"]
        niche = p.get("niche", "general")

        # Amazon data
        amazon_data = get_amazon_product_data(p["name"])
        amazon_price = amazon_data["price"]

        # Smart pricing
        recommended_price = calculate_price(
            amazon_price,
            amazon_data["competition"]
        )

        profit = recommended_price - supplier_price
        trend_score = get_trend_score(niche)

        product_data = {
            "name": p["name"],
            "supplier_price": supplier_price,
            "amazon_price": amazon_price,
            "recommended_price": recommended_price,
            "profit": round(profit, 2),
            "niche": niche,
            "trend_score": trend_score,
            "rating": amazon_data["rating"],
            "reviews": amazon_data["reviews"],
            "competition": amazon_data["competition"]
        }

        # Risk analysis
        risk = analyze_risk(product_data)
        product_data["risk"] = risk

        # Score
        score = score_product(product_data, trend_score)

        if score >= 6:
            product_data["score"] = score
            winners.append(product_data)

    return winners
