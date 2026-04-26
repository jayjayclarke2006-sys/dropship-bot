from app.amazon_sp_api import AmazonSPAPI
from app.supplier import SupplierClient
from app.db import SessionLocal, OrderRecord

def sync_orders():
    amazon = AmazonSPAPI()
    supplier = SupplierClient()
    db = SessionLocal()

    orders = amazon.get_orders()
    synced = 0

    for o in orders:
        amazon_order_id = o.get("AmazonOrderId")
        if not amazon_order_id:
            continue

        existing = db.query(OrderRecord).filter_by(amazon_order_id=amazon_order_id).first()
        if existing:
            continue

        record = OrderRecord(
            amazon_order_id=amazon_order_id,
            status=o.get("OrderStatus", "unknown"),
            fulfilment_status="pending"
        )
        db.add(record)
        synced += 1

    db.commit()
    db.close()
    return synced
