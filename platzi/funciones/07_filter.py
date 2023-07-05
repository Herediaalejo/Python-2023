numbers = [1,2,3,4,5,6]

new_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Filter no debe modificar el estado original de la lista al igual que map
print(new_numbers)

