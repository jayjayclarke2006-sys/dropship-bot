import random

def generate_listing(product):
    name = product["name"]
    price = product["amazon_price"]
    profit = product["profit"]

    # Generate title
    title = f"{name} | High Quality & Fast Shipping"

    # Bullet points
    bullets = [
        f"✅ Premium quality {name.lower()}",
        f"🔥 High demand product in {product['niche']} niche",
        f"💰 Estimated profit margin: ${profit}",
        "🚚 Fast and reliable shipping",
        "⭐ Trusted and trending product"
    ]

    # Description
    description = f"""
Introducing our top-selling {name}!

This product is currently trending in the {product['niche']} market and offers excellent value.

✔ Affordable sourcing price
✔ Strong resale potential
✔ High customer demand

Don't miss out on this winning product!
"""

    # Pricing strategy
    recommended_price = round(price * random.uniform(1.05, 1.2), 2)

    return {
        "title": title,
        "bullets": bullets,
        "description": description,
        "recommended_price": recommended_price
    }
