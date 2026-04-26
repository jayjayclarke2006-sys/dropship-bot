def find_products():
    supplier_products = [
        {"name": "Wireless Earbuds", "supplier_price": 12},
        {"name": "Phone Holder", "supplier_price": 3},
        {"name": "LED Strip Lights", "supplier_price": 8}
    ]

    amazon_prices = {
        "Wireless Earbuds": 29.99,
        "Phone Holder": 14.99,
        "LED Strip Lights": 25.99
    }

    profitable = []

    for p in supplier_products:
        amazon_price = amazon_prices.get(p["name"], 0)
        profit = amazon_price - p["supplier_price"]

        if profit > 10:
            profitable.append({
                "name": p["name"],
                "supplier_price": p["supplier_price"],
                "amazon_price": amazon_price,
                "profit": round(profit, 2)
            })

    return profitable
