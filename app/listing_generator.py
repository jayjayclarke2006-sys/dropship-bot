def generate_listing(product):
    title = product.get("title") or product.get("name") or "Trending Product"
    price = product.get("price", 19.99)
    profit = product.get("profit", 0)

    bullets = [
        "High demand product selected by automated research",
        f"Estimated profit opportunity: ${profit}",
        "Useful everyday product for online shoppers",
        "Supplier product with resale potential",
        "Review Amazon compliance before publishing"
    ]

    description = (
        f"{title} is a supplier product selected by the automation system. "
        f"It was chosen based on supplier pricing, resale potential, and product demand signals. "
        f"Please review images, delivery time, compliance, and category rules before publishing live."
    )

    return {
        "title": title[:190],
        "price": price,
        "profit": profit,
        "bullets": bullets,
        "description": description,
        "brand": "Generic",
        "product_type": "PRODUCT"
    }
