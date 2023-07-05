def increment(x):
    return x + 1

increment_v2 = lambda x: x+1

# Higher order function: Una función de Orden Superior o en sus siglas HOF se le llama así solo cuando contiene otras funciones como parámetro de entrada o devuelve una función como salida
def high_order_func(x, func):
    return x + func(x)

high_order_func_v2 = lambda x, func: x + func(x)

result = high_order_func(2, increment)
print(result)

result = high_order_func_v2(2, increment_v2)
print(result)

result = high_order_func_v2(2, lambda x: x+1) # Aquí podemos ver la ventaja de usar lambda functions, podemos definirlas a la hora de pasar el argumento a una función que recibe funciones
print(result)

result = high_order_func_v2(2, lambda x: x*2)
print(result)

result = high_order_func_v2(2, lambda x: x*5)
print(result)


