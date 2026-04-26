from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from app.config import settings

connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}

engine = create_engine(settings.database_url, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class ProductCandidate(Base):
    __tablename__ = "product_candidates"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    source = Column(String)
    supplier_sku = Column(String, nullable=True)
    supplier_cost = Column(Float, default=0)
    estimated_sell_price = Column(Float, default=0)
    estimated_fees = Column(Float, default=0)
    estimated_margin = Column(Float, default=0)
    demand_score = Column(Float, default=0)
    competition_score = Column(Float, default=0)
    fulfilment_risk_score = Column(Float, default=0)
    total_score = Column(Float, default=0)
    approved_for_listing = Column(Boolean, default=False)
    listing_status = Column(String, default="draft")
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

class ListingDraft(Base):
    __tablename__ = "listing_drafts"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, index=True)
    sku = Column(String, unique=True, index=True)
    title = Column(String)
    bullet_1 = Column(String)
    bullet_2 = Column(String)
    bullet_3 = Column(String)
    description = Column(Text)
    price = Column(Float)
    status = Column(String, default="draft")
    created_at = Column(DateTime, default=datetime.utcnow)

class OrderRecord(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    amazon_order_id = Column(String, unique=True, index=True)
    status = Column(String)
    fulfilment_status = Column(String, default="pending")
    supplier_order_id = Column(String, nullable=True)
    tracking_number = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(engine)
