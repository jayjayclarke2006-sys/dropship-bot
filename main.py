from app.product_research import find_products
from app.telegram_bot import send_telegram_message
import time


def run_bot():
    print("🚀 Bot started...")

    while True:
        try:
            print("🔍 Scanning for products...")

            products = find_products()

            if not products:
                print("❌ No products found")
            else:
                print("🔥 TOP 3 PRODUCTS FOUND")

                top_products = products[:3]

                for i, product in enumerate(top_products):
                    print(f"📦 Sending product #{i+1}")

                    message = f"""
🔥 {product['name']}

💰 Profit: ${product['profit']}
📊 Score: {product['score']}
⚠️ Risk: {product['risk']}
"""

                    send_telegram_message(message)

            print("⏳ Waiting 10 minutes...\n")
            time.sleep(600)

        except Exception as e:
            print("❌ ERROR:", str(e))
            time.sleep(60)


if __name__ == "__main__":
    run_bot()
