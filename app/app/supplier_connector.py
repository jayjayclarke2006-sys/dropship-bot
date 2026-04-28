import random

def get_supplier_match(product):
    amazon_price = product.get("amazon_price", 30)

    supplier_price = round(amazon_price * random.uniform(0.28, 0.48), 2)
    shipping_cost = round(random.uniform(2.99, 7.99), 2)
    total_cost = round(supplier_price + shipping_cost, 2)

    return {
        "supplier_name": "Manual Supplier Check Required",
        "supplier_price": supplier_price,
        "shipping_cost": shipping_cost,
        "total_cost": total_cost,
        "supplier_url": f"https://www.aliexpress.com/wholesale?SearchText={product['name'].replace(' ', '+')}",
        "note": "Check supplier branding, delivery time, returns, invoices, and packaging before selling."
    }
