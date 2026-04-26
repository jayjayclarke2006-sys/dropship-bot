def find_products():
    products = [
        {
            "name": "Wireless Earbuds",
            "price": 12,
            "amazon_price": 29.99
        },
        {
            "name": "Phone Holder",
            "price": 3,
            "amazon_price": 14.99
        },
        {
            "name": "Bad Product",
            "price": 20,
            "amazon_price": 22
        }
    ]

    profitable = []

    for p in products:
        profit = p["amazon_price"] - p["price"]

        if profit > 10:
            p["profit"] = round(profit, 2)
            profitable.append(p)

    return profitable
