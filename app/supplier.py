import requests

def get_supplier_products():
    url = "https://fakestoreapi.com/products"

    try:
        response = requests.get(url)
        data = response.json()

        products = []

        for item in data[:5]:  # limit to 5 products
            products.append({
                "name": item["title"],
                "supplier_price": float(item["price"])
            })

        return products

    except Exception as e:
        print("Error fetching supplier data:", e)
        return []
