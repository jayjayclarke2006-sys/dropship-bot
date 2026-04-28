import time
from app.product_engine import get_products
from app.listing_generator import generate_listing

print("🚀 AMAZON AUTO SYSTEM STARTING...")


def run_bot():
    while True:
        print("🔍 Finding products...\n")

        try:
            products = get_products()

            for product in products:
                print("📦 PRODUCT:", product["name"])

                listing = generate_listing(product)

                print("\n🧠 GENERATED LISTING:")
                print("TITLE:", listing["title"])
                print("PRICE:", listing["price"])

                print("BULLETS:")
                for b in listing["bullets"]:
                    print("-", b)

                print("DESCRIPTION:", listing["description"])
                print("\n" + "-"*40 + "\n")

        except Exception as e:
            print("❌ ERROR:", e)

        print("⏳ Waiting 10 minutes...\n")
        time.sleep(600)


if __name__ == "__main__":
    run_bot()
