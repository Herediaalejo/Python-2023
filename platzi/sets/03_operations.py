set_a = {"col", "arg", "pe"}
set_b = {"pe", "bol"}

# Union 
set_c = set_a.union(set_b) # Los elementos de ambos conjuntos.
print(set_c)

print(set_a | set_b) # Forma abreviada sin usar función.

# Intersección
set_c = set_a.intersection(set_b)# Los elementos que ambos conjuntos tienen en común.
print(set_c)

print(set_a & set_b) # Forma abreviada sin usar función.

# Diferencia

set_c = set_a.difference(set_b) # Los elementos que existen en un conjunto menos los que tienen en común.
print(set_c)

print(set_a - set_b) # Forma abreviada sin usar función.

# Diferencia simétrica

set_c = set_a.symmetric_difference(set_b) # Los elementos que existen en ambos conjuntos menos los que tienen en común.
print(set_c)

print(set_a ^ set_b) # Forma abreviada sin usar función.