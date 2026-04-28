import requests
from bs4 import BeautifulSoup
import random
import re

used_products = set()


def extract_price(text):
    match = re.search(r"\$([\d,]+\.?\d*)", text)
    if match:
        return float(match.group(1).replace(",", ""))
    return None


# ---------------- AMAZON ---------------- #

def scrape_amazon():
    headers = {"User-Agent": "Mozilla/5.0"}

    keywords = [
        "tiktok gadgets",
        "cool gadgets",
        "smart home devices",
        "tech accessories"
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

            if name in used_products or len(name) < 12:
                continue

            price = float(price_whole.text.replace(",", ""))
            if price_fraction:
                price += float("0." + price_fraction.text)

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


# ---------------- ALIEXPRESS ---------------- #

def scrape_aliexpress(product_name):
    headers = {"User-Agent": "Mozilla/5.0"}

    search = product_name.replace(" ", "+")
    url = f"https://www.aliexpress.com/wholesale?SearchText={search}"

    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        prices = []

        for tag in soup.select("span"):
            text = tag.get_text()
            if "$" in text:
                price = extract_price(text)
                if price and price > 1:
                    prices.append(price)

        if prices:
            return round(min(prices), 2)

    except:
        pass

    return None


# ---------------- SCORING ---------------- #

def trend_score(name):
    keywords = ["mini", "smart", "portable", "wireless", "led", "usb", "pro"]
    score = random.uniform(5, 10)

    for word in keywords:
        if word in name.lower():
            score += 1.5

    return round(score, 2)


def calculate_score(profit, trend):
    return round((profit * 0.8) + (trend * 2), 2)


# ---------------- MAIN ---------------- #

def find_products():
    products = scrape_amazon()

    if len(products) < 3:
        products = [
            {"name": "Mini Projector", "amazon_price": 79.99},
            {"name": "Smart Watch", "amazon_price": 49.99},
            {"name": "Wireless Earbuds", "amazon_price": 29.99}
        ]

    final = []

    for item in products:
        name = item["name"]
        amazon_price = item["amazon_price"]

        supplier_price = scrape_aliexpress(name)

        if not supplier_price:
            supplier_price = round(amazon_price * random.uniform(0.3, 0.5), 2)

        profit = round(amazon_price - supplier_price, 2)

        # 🚨 STRICT FILTER (important)
        if profit < 15:
            continue

        trend = trend_score(name)
        score = calculate_score(profit, trend)

        product = {
            "name": name,
            "amazon_price": amazon_price,
            "supplier_price": supplier_price,
            "profit": profit,
            "score": score,
            "trend_score": trend,
            "risk": "low" if profit > 25 else "medium",
            "link": f"https://www.amazon.com/s?k={name.replace(' ', '+')}",
            "image": f"https://source.unsplash.com/400x400/?{name.replace(' ', '')}"
        }

        final.append(product)

    return sorted(final, key=lambda x: x["score"], reverse=True)[:3]
