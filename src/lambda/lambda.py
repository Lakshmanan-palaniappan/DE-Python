products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 600}
]

sorted_products = sorted(products, key=lambda x: x["price"])
print(sorted_products)
