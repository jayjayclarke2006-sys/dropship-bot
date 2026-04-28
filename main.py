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
                print("🔥 TOP PRODUCTS FOUND")

                sent = 0

                for product in products:

                    # 🔥 FILTER (ONLY GOOD PRODUCTS)
                    if product["profit"] < 20 or product["score"] < 35:
                        continue

                    print(f"📦 Sending: {product['name']}")

                    message = f"""
🔥 *{product['name']}*

💰 Profit: ${product['profit']}
📊 Score: {product['score']}
⚠️ Risk: {product['risk']}

🛒 [View on Amazon]({product['link']})
"""

                    send_telegram_message(message)

                    sent += 1

                    if sent == 3:
                        break

            print("⏳ Waiting 10 minutes...\n")
            time.sleep(600)

        except Exception as e:
            print("❌ ERROR:", str(e))
            time.sleep(60)


if __name__ == "__main__":
    run_bot()
