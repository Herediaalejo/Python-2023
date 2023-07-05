items = [
    {
        "product": "camisa",
        "price" : 100,
    },
    {
        "product": "pantalones",
        "price": 300
    },
    {
        "product": "chaqueta",
        "price": 500
    }
]

prices = list(map(lambda item: item["price"], items))

print(prices)

def add_taxes(item):
    new_item = item.copy() # Hago una copia del diccionario original para que no compartan la misma dirección en memoria y por lo tanto no se modifique el array original
    new_item["taxes"] = new_item["price"] * .19
    return new_item

new_items = list(map(add_taxes, items))

print("New list")
print(new_items)
print("Old list")
print(items)

numbers = [1, 2, 3, 4]
response = list(map(lambda num: num * 2, numbers))
print(response)