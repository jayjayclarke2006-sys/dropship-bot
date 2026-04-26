import random

def get_supplier_products():
    return [
        {"name": "Wireless Earbuds", "supplier_price": random.randint(8, 15)},
        {"name": "Phone Holder", "supplier_price": random.randint(2, 6)},
        {"name": "LED Strip Lights", "supplier_price": random.randint(5, 10)},
        {"name": "Bluetooth Speaker", "supplier_price": random.randint(10, 20)},
    ]
