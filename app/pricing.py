import random

def calculate_price(amazon_price, competition):
    # Undercut competitors slightly if high competition
    if competition == "high":
        return round(amazon_price * random.uniform(0.90, 0.95), 2)

    elif competition == "medium":
        return round(amazon_price * random.uniform(0.95, 1.0), 2)

    else:  # low competition
        return round(amazon_price * random.uniform(1.0, 1.1), 2)


def analyze_risk(product):
    risk = "low"

    if product["competition"] == "high":
        risk = "high"
    elif product["reviews"] > 1000:
        risk = "medium"

    if product["profit"] < 10:
        risk = "high"

    return risk
