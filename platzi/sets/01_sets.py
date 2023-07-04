set_countries = {"col", "mex", "bol"}
#Los conjuntos son tipos de datos que pueden ser modificados, no están ordenados y no contienen elementos iguales
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,2,3242,53235}
print(set_numbers)

set_types = {1, False, "hola", 23.12}
print(set_types)

set_from_string = set(" hoooolaaa ")
print(set_from_string)
#El conjunto divide la palabra en caracteres y saca los caracteres iguales

set_from_tuples = set(("adc", "dfs", "ads", "bca", "ads"))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
#Nos sirve para obtener los números únicos que no se repiten
unique_numbers = list(set_numbers)
print(unique_numbers)