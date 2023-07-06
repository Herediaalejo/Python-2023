try:
    print(0 / 0)
    assert 1!=1, "Uno es igual a uno"
    age = 10
    if age < 18:
        raise Exception("No se permiten menores de edad") 
except Exception as error:
    print(error) # Imprimo el error sin detener el programa
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
else:
    print("Este se ejecuta solo si no hay excepts")
finally:
    print("Este se ejecuta siempre")

print("Hola")


    
    