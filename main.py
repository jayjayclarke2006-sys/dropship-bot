from app.telegram_bot import send_telegram_message

def run_bot():
    while True:
        print("🔍 Scanning for products...")

        products = find_products()

        if not products:
            print("❌ No good products found")
        else:
            best = products[0]
            print("🔥 BEST PRODUCT FOUND:", best)

            listing = generate_listing(best)
            print("📦 GENERATED LISTING:", listing)

            # 🚀 SEND TO TELEGRAM
            message = f"""
🔥 BEST PRODUCT FOUND

📦 {best['name']}
💰 Profit: ${best['profit']}
📊 Score: {best['score']}
📈 Trend: {best['trend_score']}
⚠️ Risk: {best['risk']}

🛒 PRICE: ${best['amazon_price']}

-----------------------

📝 LISTING:

{listing['title']}

{listing['description']}
"""
            send_telegram_message(message)

        print("⏳ Waiting 10 minutes...\n")
        time.sleep(600)
