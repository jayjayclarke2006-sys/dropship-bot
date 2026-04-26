from app.product_research import research_products
from app.listing_generator import create_listing_drafts
from app.order_sync import sync_orders

def run_all_jobs():
    products = research_products()
    drafts = create_listing_drafts()
    orders = sync_orders()

    print(f"Job complete: {products} product candidates, {drafts} listing drafts, {orders} orders synced.")
