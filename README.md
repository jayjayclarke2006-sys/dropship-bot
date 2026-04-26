# Amazon Dropshipping Automation System

A compliant starter system for Amazon dropshipping automation.

## What it does

- Finds product ideas from configurable trend/supplier sources
- Scores products by demand, margin, competition, and fulfilment risk
- Creates listing drafts
- Has Amazon SP-API integration stubs for listings and orders
- Has supplier fulfilment hooks
- Runs automatically with a scheduler
- Can deploy to Railway, Render, Replit, or any VPS

## Important compliance notes

Amazon dropshipping must follow Amazon policy:
- You must be the seller of record.
- Your supplier must not appear on packing slips, invoices, packaging, or external labels.
- You are responsible for customer returns.
- Use Amazon Selling Partner API, not page scraping.

## Quick start locally

```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# Windows: .venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
python main.py
```

Open the local API:

```bash
uvicorn app.api:app --reload
```

Then visit:

```text
http://127.0.0.1:8000/products
```

## Deploy on Railway

1. Create a GitHub repo.
2. Upload this folder.
3. Go to Railway.
4. New Project -> Deploy from GitHub.
5. Add PostgreSQL.
6. Add environment variables from `.env.example`.
7. Set start command:

```bash
python main.py
```

For API deployment instead:

```bash
uvicorn app.api:app --host 0.0.0.0 --port $PORT
```

## Phone setup

You can do this from your phone with:

- Replit mobile app: easiest
- GitHub mobile + Railway dashboard: possible
- Termux on Android: possible but harder

Best phone path:
1. Upload ZIP to Replit.
2. Add `.env`.
3. Press Run.
4. Upgrade to an always-on/Reserved VM style plan if you need 24/7.

## Amazon SP-API credentials needed

You will need:

- LWA Client ID
- LWA Client Secret
- Refresh Token
- AWS Access Key
- AWS Secret Key
- Role ARN
- Seller ID
- Marketplace ID

This starter includes placeholders. Do not commit real secrets.
