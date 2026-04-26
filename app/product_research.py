from app.supplier import get_supplier_products
import random

def estimate_amazon_price(supplier_price):
    return round(supplier_price * random.uniform(2.5, 4.5), 2)


def find_products():
    supplier_products = get_supplier_products()

    profitable = []

    for p in supplier_products:
        amazon_price = estimate_amazon_price(p["supplier_price"])
        profit = amazon_price - p["supplier_price"]

        if profit > 10:
            profitable.append({
                "name": p["name"],
                "supplier_price": p["supplier_price"],
                "amazon_price": amazon_price,
                "profit": round(profit, 2)
            })

    return profitable
