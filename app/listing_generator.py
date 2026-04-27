def generate_listing(product):
    name = product["name"]
    niche = product.get("niche", "general")
    recommended_price = product.get("amazon_price", 0)
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

    description = (
        f"{name} is a high-potential product in the {niche} niche. "
        f"This product has been selected using automated scoring based on profit, trends, "
        f"and demand. Ideal for reselling with strong margins."
    )

    return {
        "title": title,
        "bullets": bullets,
        "description": description,
        "recommended_price": recommended_price
    }
