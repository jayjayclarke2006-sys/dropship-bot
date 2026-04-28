def generate_listing(product):
    name = product["name"]
    niche = product.get("niche", "tech")
    price = product.get("amazon_price", product.get("sell_price", 29.99))
    profit = product.get("profit", 0)
    score = product.get("score", 0)
    risk = product.get("risk", "medium")

    title = f"{name} - Trending {niche.title()} Product for Everyday Use"

    bullets = [
        f"Trending {niche} product with strong customer demand",
        f"Estimated profit potential: ${profit}",
        f"Product score: {score}",
        f"Risk level: {risk}",
        "Ideal for online retail, gifting, and everyday use"
    ]

    description = f"""
{name} is a high-potential product selected by your automated product research system.

This listing was generated based on:
- Estimated profit
- Trend score
- Product demand
- Risk level
- Resale potential

Before uploading to Amazon, check:
- Category restrictions
- Brand/IP restrictions
- Supplier delivery time
- UPC/GTIN requirements
- Amazon dropshipping policy
"""

    keywords = f"{name}, {niche}, trending product, online shopping, gadget, gift"

    return {
        "title": title,
        "price": round(price, 2),
        "bullets": bullets,
        "description": description.strip(),
        "keywords": keywords
    }
