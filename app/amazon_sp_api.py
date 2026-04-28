import os
import requests

SELLER_ID = os.getenv("AMAZON_SELLER_ID")
MARKETPLACE_ID = os.getenv("AMAZON_MARKETPLACE_ID", "A1F83G8C2ARO7P")
SP_API_ACCESS_TOKEN = os.getenv("SP_API_ACCESS_TOKEN")


def amazon_ready():
    return bool(SELLER_ID and MARKETPLACE_ID and SP_API_ACCESS_TOKEN)


def create_amazon_listing_payload(product, listing):
    sku = product["name"].upper().replace(" ", "-")[:35]

    return {
        "sku": sku,
        "marketplace_id": MARKETPLACE_ID,
        "product_name": listing["title"],
        "price": listing["price"],
        "bullets": listing["bullets"],
        "description": listing["description"],
        "keywords": listing["keywords"],
        "status": "DRAFT_ONLY",
        "note": (
            "This payload is prepared for SP-API, but not submitted unless "
            "valid product type schema, GTIN/ASIN, category approval, and credentials exist."
        )
    }


def submit_listing_to_amazon(product, listing):
    if not amazon_ready():
        return {
            "submitted": False,
            "reason": "Amazon SP-API credentials not configured yet.",
            "payload": create_amazon_listing_payload(product, listing)
        }

    # IMPORTANT:
    # Real SP-API listing creation requires signed requests, product type schema,
    # valid attributes, GTIN/ASIN, and Product Listing role approval.
    # Keep this as a safe placeholder until your SP-API app is fully approved.
    return {
        "submitted": False,
        "reason": "SP-API placeholder active. Ready for real Listings Items API wiring.",
        "payload": create_amazon_listing_payload(product, listing)
    }
