import requests
from bs4 import BeautifulSoup
import random
import re

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


def extract_price(text):
    match = re.search(r"\$([\d,]+\.?\d*)", text)
    if match:
        return float(match.group(1).replace(",", ""))
    return None


def scrape_amazon():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    keywords = [
        "tiktok gadgets",
        "cool gadgets",
        "smart home devices",
        "tech accessories",
        "amazon best sellers gadgets"
    ]

    search = random.choice(keywords)
    url = f"https://www.amazon.com/s?k={search.replace(' ', '+')}"

    results = []

    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        items = soup.select(".s-result-item")

        for item in items:
            title_tag = item.select_one("h2 a span")
            price_whole = item.select_one(".a-price-whole")
            price_fraction = item.select_one(".a-price-fraction")

            if not title_tag or not price_whole:
                continue

            name = title_tag.text.strip()

            if len(name) < 12 or name in used_products:
                continue

            price = float(price_whole.text.replace(",", ""))
            if price_fraction:
                price += float("0." + price_fraction.text)

            # Skip cheap junk
            if price < 15:
                continue

            used_products.add(name)

            results.append({
                "name": name,
                "amazon_price": round(price, 2)
            })

            if len(results) >= 5:
                break

    except:
        pass

    return results


def fallback_products():
    return [
        {"name": "Mini Projector", "amazon_price": 79.99},
        {"name": "Smart Watch", "amazon_price": 49.99},
        {"name": "Wireless Earbuds", "amazon_price": 29.99},
        {"name": "Bluetooth Speaker", "amazon_price": 39.99},
        {"name": "Portable Blender", "amazon_price": 34.99}
    ]


def estimate_supplier_price(amazon_price):
    return round(amazon_price * random.uniform(0.25, 0.45), 2)


def find_products():
    scraped = scrape_amazon()

    if len(scraped) < 3:
        scraped = fallback_products()

    selected = random.sample(scraped, 3)

    results = []

    for item in selected:
        name = item["name"]
        amazon_price = item["amazon_price"]

        supplier_price = estimate_supplier_price(amazon_price)
        profit = round(amazon_price - supplier_price, 2)

        trend_score = calculate_trend_score(name)
        score = calculate_score(profit, trend_score)

        # Filter weak products
        if profit < 12:
            continue

        product = {
            "name": name,
            "supplier_price": supplier_price,
            "amazon_price": amazon_price,
            "profit": profit,
            "trend_score": trend_score,
            "score": score,
            "niche": "tech",
            "risk": "low" if profit > 20 else "medium",
            "image": f"https://source.unsplash.com/400x400/?{name.replace(' ', '')}",
            "link": f"https://www.amazon.com/s?k={name.replace(' ', '+')}"
        }

        results.append(product)

    return sorted(results, key=lambda x: x["score"], reverse=True)
