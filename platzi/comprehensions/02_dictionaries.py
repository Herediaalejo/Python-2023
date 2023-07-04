import random

dict = {}

for i in range(1,5):
    dict[i] = i*2

print(dict)

dict_v2 = {i:i * 2 for i in range (1,5)}

print(dict_v2)

#--------------------------------------------------------------------------

countries = ["col", "arg", "uru"]
population = {}
for country in countries:
    population[country] = random.randint(1,100)

print(population)

population_v2 = {country: random.randint(1,100) for country in countries}

print(population_v2)

population_v3 = {country: population for (country,population) in population_v2.items() if population >= 50}

print(population_v3)

#--------------------------------------------------------------------------

names = ["ale", "lucas", "ivo"]
ages = [20, 15, 25]

new_dict = {}

for i in range(len(names)):
  new_dict[names[i]] = ages[i]

print(new_dict)

print(list(zip(names,ages))) #Con zip puedo unir dos listas diferentes

new_dict = {name: age for name,age in zip(names,ages)}

print(new_dict)

new_dict = {names[i]:ages[i] for i in range(len(names))}

print(new_dict)

# Ambas son comprehensions y son validas

#--------------------------------------------------------------------------

text = "Hola soy Alejo"

dict_vocals = { vocal: vocal.upper() for vocal in text if vocal in "aeiou"}

print(dict_vocals)