def generate_listing(product):
    name = product["name"]
    niche = product.get("niche", "general")
    recommended_price = product.get("recommended_price", product.get("amazon_price", 0))
    profit = product.get("profit", 0)
    score = product.get("score", 0)
    risk = product.get("risk", "unknown")

    title = f"{name} - Trending {niche.title()} Product"

    bullets = [
        f"Designed for customers interested in {niche} products.",
        "Selected using automated product scoring and demand analysis.",
        f"Estimated profit: ${profit}.",
        f"Product score: {score}.",
        f"Risk level: {risk}."
    ]

    description = (
        f"{name} is a high-potential product identified by the automation system. "
        f"It falls under the {niche} niche and has been selected based on profit margins, "
        f"trend analysis, competition level, and risk scoring. "
        f"Ensure supplier reliability and delivery time before listing."
    )

    return {
        "title": title,
        "bullets": bullets,
        "description": description,
        "recommended_price": recommended_price
    }
