import random

def get_supplier_products():
    return [
        {"name": "Wireless Earbuds", "supplier_price": random.randint(8, 15)},
        {"name": "Phone Holder", "supplier_price": random.randint(2, 6)},
        {"name": "LED Strip Lights", "supplier_price": random.randint(5, 10)},
        {"name": "Bluetooth Speaker", "supplier_price": random.randint(10, 20)},
    ]


def find_products():
    supplier_products = get_supplier_products()

    amazon_prices = {
        "Wireless Earbuds": 29.99,
        "Phone Holder": 14.99,
        "LED Strip Lights": 25.99,
        "Bluetooth Speaker": 39.99
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
