import random

def get_supplier_products():
    return [
        {"name": "Wireless Earbuds", "supplier_price": random.randint(8, 15), "niche": "tech"},
        {"name": "Phone Holder", "supplier_price": random.randint(2, 6), "niche": "car"},
        {"name": "LED Strip Lights", "supplier_price": random.randint(5, 10), "niche": "home"},
        {"name": "Bluetooth Speaker", "supplier_price": random.randint(10, 20), "niche": "tech"},
        {"name": "Mini Projector", "supplier_price": random.randint(20, 40), "niche": "tech"},
        {"name": "Car Vacuum Cleaner", "supplier_price": random.randint(10, 25), "niche": "car"},
        {"name": "Smart Watch", "supplier_price": random.randint(15, 35), "niche": "tech"},
        {"name": "Gaming Mouse", "supplier_price": random.randint(5, 15), "niche": "gaming"},
    ]
