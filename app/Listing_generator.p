def generate_listing(product):
    name = product["name"]
    niche = product.get("niche", "general")
    recommended_price = product.get("recommended_price", product.get("amazon_price", 0))
    profit = product.get("profit", 0)
    score = product.get("score", 0)
    trend_score = product.get("trend_score", 0)

    # 🔥 SEO-style title (better for Amazon)
    title = f"{name} for Everyday Use | High Quality {niche.title()} Product | Fast Shipping"

    # 🔥 Sales-focused bullet points
    bullets = [
        f"🔥 Trending {niche} product with strong demand",
        f"💰 High resale potential with estimated profit of ${profit}",
        "⚡ Designed for convenience, durability, and everyday use",
        "🚚 Fast shipping and reliable quality",
        "⭐ Perfect for customers looking for value and performance"
    ]

    # 🔥 Conversion-focused description
    description = (
        f"Introducing the {name}, one of the fastest-growing products in the {niche} niche.\n\n"
        f"This product is currently gaining traction due to its combination of affordability, "
        f"high demand, and strong resale margins.\n\n"
        f"✔ Trending product with increasing demand\n"
        f"✔ Ideal for reselling and dropshipping\n"
        f"✔ Competitive pricing and strong profit margins\n\n"
        f"Don't miss out on adding this high-potential product to your store."
    )

    # 🔥 Pricing strategy (cleaned up)
    final_price = round(recommended_price, 2)

    return {
        "title": title,
        "bullets": bullets,
        "description": description,
        "recommended_price": final_price
    }
