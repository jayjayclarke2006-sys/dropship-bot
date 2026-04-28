import random

used_products = set()

def calculate_score(profit, trend_score):
    return round((profit * 0.7) + (trend_score * 3), 2)


def calculate_trend_score(name):
    keywords = ["mini", "smart", "portable", "wireless", "led", "usb", "pro", "max"]

    score = random.uniform(5, 10)

    for word in keywords:
        if word in name.lower():
            score += 1.5

    return round(score, 2)


def find_products():
    base_products = [
        "Mini Projector",
        "Smart Watch",
        "Wireless Earbuds",
        "LED Strip Lights",
        "Bluetooth Speaker",
        "Portable Blender",
        "Car Vacuum Cleaner",
        "Gaming Headset",
        "Phone Cooling Fan",
        "Smart Ring",
        "USB Mini Fan",
        "Magnetic Charger",
        "Desk LED Lamp",
        "Portable Power Bank",
        "Noise Cancelling Headphones"
    ]

    # Avoid repeats
    available = [p for p in base_products if p not in used_products]

    if len(available) < 3:
        used_products.clear()
        available = base_products

    selected = random.sample(available, 3)

    results = []

    for name in selected:
        used_products.add(name)

        supplier_price = round(random.uniform(8, 30), 2)
        amazon_price = round(supplier_price * random.uniform(2.2, 3.5), 2)
        profit = round(amazon_price - supplier_price, 2)

        trend_score = calculate_trend_score(name)
        score = calculate_score(profit, trend_score)

        risk = "low" if profit > 20 else "medium"

        product = {
            "name": name,
            "supplier_price": supplier_price,
            "amazon_price": amazon_price,
            "profit": profit,
            "trend_score": trend_score,
            "score": score,
            "niche": "tech",
            "risk": risk,
            "image": f"https://source.unsplash.com/400x400/?{name.replace(' ', '')}"
        }

        results.append(product)

    # Sort best first
    return sorted(results, key=lambda x: x["score"], reverse=True)
