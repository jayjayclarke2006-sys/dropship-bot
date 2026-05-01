def main():
    print("🚀 Bot started...")

    while True:
        try:
            # 🔥 STEP 1: Try Amazon (but DON'T crash if it fails)
            try:
                token = get_amazon_access_token()
                print("✅ Amazon token OK")
            except Exception as e:
                print("❌ Amazon error:", e)
                token = None  # continue anyway

            # 🔥 STEP 2: Get products
            products = find_products()
            print(f"Found {len(products)} products")

            # 🔥 STEP 3: Send to Telegram (ALWAYS runs)
            for product in products:
                msg = format_product(product)
                send_telegram_message(msg)
                time.sleep(2)

        except Exception as e:
            print("🔥 MAIN LOOP ERROR:", e)

        time.sleep(300)
