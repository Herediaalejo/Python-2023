dict = {"palabras lindas": "amanecer", "palabras feas": "gil", "hola": "chau"}

dict2 = {key: value for key, value in dict.items() if "palabras" in key}
print(dict2)