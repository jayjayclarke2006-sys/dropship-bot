from app.supplier import get_supplier_products

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

        if profit > 5:
            profitable.append({
                "name": p["name"],
                "supplier_price": p["supplier_price"],
                "amazon_price": amazon_price,
                "profit": round(profit, 2),
                "niche": "gadgets"
            })

    return profitable
