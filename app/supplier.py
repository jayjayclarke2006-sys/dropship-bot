import requests

def get_supplier_products():
    url = "https://fakestoreapi.com/products"

    try:
        response = requests.get(url)
        data = response.json()

        products = []

        for item in data[:10]:  # limit to 10 products
            products.append({
                "name": item["title"],
                "supplier_price": float(item["price"]),
                "niche": item["category"]
            })

        return products

    except Exception as e:
        print("Error fetching supplier data:", e)
        return []
