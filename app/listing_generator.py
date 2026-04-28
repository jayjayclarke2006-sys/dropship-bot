def generate_listing(product):
    name = product["name"]
    niche = product.get("niche", "general")
    recommended_price = product.get("sell_price", product.get("amazon_price", 29.99))
    profit = product.get("profit", 0)
    score = product.get("score", 0)
    risk = product.get("risk", "unknown")

    title = f"{name} - Trending {niche.title()} Product"

    bullets = [
        f"🔥 Trending in {niche} niche",
        f"💰 Estimated profit: ${profit}",
        f"📊 Product score: {score}",
        f"⚠️ Risk level: {risk}",
        "🚀 Fast shipping & high demand"
    ]

    description = f"""
{name} is a high-potential product in the {niche} niche.

This product has been selected using automated scoring based on profit, trends, and demand.

✔ Strong margins  
✔ High demand  
✔ Easy to sell  

Perfect for reselling and scaling.
"""

    return {
        "title": title,
        "price": recommended_price,
        "bullets": bullets,
        "description": description
    }
