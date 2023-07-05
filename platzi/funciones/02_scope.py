price = 100 # Alcance global


def increment():
    price = 100 # Alcance local
    price = price + 10 
    return(price)


print(price)
price_2 = increment()
print(price_2)