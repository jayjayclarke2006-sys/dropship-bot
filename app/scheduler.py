import time
from app.product_research import find_products
from app.notifier import send_alert


def run_bot():
    while True:
        print("🔍 Scanning for products...")

        products = find_products()

        if products:
            best = products[0]
            print("🔥 BEST PRODUCT FOUND:")
            print(best)

            # 🚨 SEND TELEGRAM ALERT
            send_alert(best)

        else:
            print("❌ No good products found")

        print("⏳ Waiting 10 minutes...\n")
        time.sleep(600)
