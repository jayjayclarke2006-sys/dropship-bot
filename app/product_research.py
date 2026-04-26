import random
from app.config import settings
from app.db import SessionLocal, ProductCandidate

TREND_FEED = [
    "portable desk fan",
    "magnetic car phone holder",
    "travel cable organizer",
    "under desk foot rest",
    "reusable lint roller",
    "shoe cleaning kit",
    "laptop stand adjustable",
    "pet hair remover brush",
    "silicone air fryer liners",
    "mini humidifier usb"
]

def get_trending_product_names():
    # Replace this with licensed/allowed data sources:
    # Google Trends, supplier APIs, wholesale feeds, Keepa, Helium10, JungleScout, etc.
    return TREND_FEED

def estimate_numbers(name: str):
    supplier_cost = round(random.uniform(4.0, 18.0), 2)
    sell_price = round(supplier_cost * random.uniform(2.0, 3.2), 2)
    amazon_fee = round(sell_price * 0.15, 2)
    shipping_allowance = round(random.uniform(1.0, 4.0), 2)
    profit = sell_price - supplier_cost - amazon_fee - shipping_allowance
    margin = profit / sell_price if sell_price else 0

    demand = random.uniform(0.45, 0.95)
    competition = random.uniform(0.20, 0.90)
    fulfilment_risk = random.uniform(0.05, 0.55)

    score = (demand * 0.45) + (margin * 0.35) - (competition * 0.20) - (fulfilment_risk * 0.25)

    return {
        "supplier_cost": round(supplier_cost, 2),
        "estimated_sell_price": round(sell_price, 2),
        "estimated_fees": round(amazon_fee + shipping_allowance, 2),
        "estimated_margin": round(margin, 3),
        "demand_score": round(demand, 3),
        "competition_score": round(competition, 3),
        "fulfilment_risk_score": round(fulfilment_risk, 3),
        "total_score": round(score, 3),
    }

def research_products():
    db = SessionLocal()
    created = 0

    for name in get_trending_product_names():
        nums = estimate_numbers(name)

        if nums["estimated_margin"] < settings.min_margin:
            continue
        if nums["total_score"] < settings.min_score:
            continue

        product = ProductCandidate(
            name=name,
            source="trend_feed",
            supplier_sku=f"SUP-{name[:4].upper()}-{random.randint(1000,9999)}",
            **nums,
            notes="Needs manual restriction/gating/IP/supplier checks before listing."
        )
        db.add(product)
        created += 1

    db.commit()
    db.close()
    return created
