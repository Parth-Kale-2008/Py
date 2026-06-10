products = {
    "soap":50,
    "agarbatti":.130,
    "oreo":10,
    "bmw m5":40000000
}

expensive_products = max(products,key=products.get)
print("Product with highest price:", expensive_products,"the price is ",products[expensive_products])
#print("Price:", products[expensive_products])