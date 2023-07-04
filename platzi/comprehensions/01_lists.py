numbers = []

for element in range(1,11):
    numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1,11)]

print(numbers_v2)

# Obtenemos el mismo resultado

numbers2 = []

for element in range(1,11):
    if element % 2 == 0:
        numbers2.append(element * 2)

print(numbers2)

numbers2_v2 = [element * 2 for element in range(1,11) if element % 2 == 0]

print(numbers2_v2)

# Obtenemos el mismo resultado

x = int(input())
y = int(input())
z = int(input())
n = int(input())

list = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i + j + k != n:
                list.append([i,j,k])
                
print(list)

list_v2 = [[i,j,k] for i in range(x+1) for j in range (y+1) for k in range (z+1) if i+j+k != n]

print(list_v2)

# Obtenemos el mismo resultado
