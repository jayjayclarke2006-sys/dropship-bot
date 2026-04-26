from fastapi import FastAPI
from app.db import init_db, SessionLocal, ProductCandidate, ListingDraft, OrderRecord
from app.jobs import run_all_jobs

app = FastAPI(title="Amazon Dropshipping Automation System")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def home():
    return {"status": "ok", "service": "dropship-automation"}

@app.post("/run")
def run_now():
    run_all_jobs()
    return {"status": "jobs completed"}

@app.get("/products")
def products():
    db = SessionLocal()
    rows = db.query(ProductCandidate).order_by(ProductCandidate.total_score.desc()).limit(100).all()
    data = [
        {
            "id": r.id,
            "name": r.name,
            "source": r.source,
            "margin": r.estimated_margin,
            "score": r.total_score,
            "sell_price": r.estimated_sell_price,
            "notes": r.notes,
        }
        for r in rows
    ]
    db.close()
    return data

@app.get("/drafts")
def drafts():
    db = SessionLocal()
    rows = db.query(ListingDraft).order_by(ListingDraft.created_at.desc()).limit(100).all()
    data = [
        {
            "id": r.id,
            "sku": r.sku,
            "title": r.title,
            "price": r.price,
            "status": r.status,
        }
        for r in rows
    ]
    db.close()
    return data

@app.get("/orders")
def orders():
    db = SessionLocal()
    rows = db.query(OrderRecord).order_by(OrderRecord.created_at.desc()).limit(100).all()
    data = [
        {
            "amazon_order_id": r.amazon_order_id,
            "status": r.status,
            "fulfilment_status": r.fulfilment_status,
            "tracking_number": r.tracking_number,
        }
        for r in rows
    ]
    db.close()
    return data
