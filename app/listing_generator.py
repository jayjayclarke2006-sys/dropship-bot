from app.db import SessionLocal, ProductCandidate, ListingDraft

def build_listing_copy(product: ProductCandidate):
    clean_name = product.name.title()
    title = f"{clean_name} - Practical Everyday Accessory"
    bullets = [
        f"Useful {clean_name.lower()} designed for daily convenience.",
        "Compact, easy to store, and suitable for home, work, or travel.",
        "Check compatibility, dimensions, and supplier quality before publishing."
    ]
    description = (
        f"This listing draft is for {clean_name}. "
        "Before publishing, confirm brand rights, product safety, category restrictions, "
        "supplier packaging, shipping time, return address, and Amazon policy compliance."
    )
    return title, bullets, description

def create_listing_drafts():
    db = SessionLocal()
    products = db.query(ProductCandidate).filter_by(approved_for_listing=False).all()
    created = 0

    for p in products:
        # In real use, require a human approval gate here.
        title, bullets, description = build_listing_copy(p)
        sku = f"DS-{p.id}-{p.name.replace(' ', '-')[:20].upper()}"

        existing = db.query(ListingDraft).filter_by(sku=sku).first()
        if existing:
            continue

        draft = ListingDraft(
            product_id=p.id,
            sku=sku,
            title=title,
            bullet_1=bullets[0],
            bullet_2=bullets[1],
            bullet_3=bullets[2],
            description=description,
            price=p.estimated_sell_price,
            status="draft"
        )
        db.add(draft)
        created += 1

    db.commit()
    db.close()
    return created
