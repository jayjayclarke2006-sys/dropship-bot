def generate_listing(product):
    name = product["name"]
    price = product.get("price", 19.99)
    profit = product.get("profit", 0)
    niche = product.get("niche", "general")

    title = f"{name} - Trending {niche.title()} Product"

    bullets = [
        "High demand product with strong resale potential",
        f"Estimated profit opportunity: ${profit}",
        "Useful everyday item for online shoppers",
        "Selected using automated product research",
        "Check supplier delivery times before publishing"
    ]

    description = (
        f"{name} is a potential selling opportunity selected by the automation system. "
        f"This product was chosen based on supplier price, estimated resale value, and demand potential. "
        f"Before publishing, review Amazon category rules, images, shipping time, and product compliance."
    )

    return {
        "title": title[:190],
        "price": price,
        "bullets": bullets,
        "description": description,
        "brand": "Generic",
        "product_type": "PRODUCT"
    }
