def validarOpcionDos(opcion):
    try:
        opcion = int(opcion)
        if opcion == 1 or opcion == 2:
            return opcion
        else:
            print("Valor fuera de rango")
            opcion = 0
            return opcion
    except ValueError:
        print("Valor invalido")
        opcion = 0
        return opcion
    
def validarOpcionCinco(opcion):
    try:
        opcion = int(opcion)
        if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
            return opcion
        else:
            print("Valor fuera de rango")
            opcion = 0
            return opcion
    except ValueError:
        print("Valor invalido")
        opcion = 0
        return opcion

agenda = {}
nombre = ""
telefono = ""
op = ""
flag = 0
buscar = ""
while True:
    op = input("""
    Bienvenido al gestor de contactos
    1. Agregar contacto
    2. Buscar contacto
    3. Eliminar contacto
    4. Mostrar todos los contactos
    5. Salir
    """)
    op = validarOpcionCinco(op)
    if op == 1:
        while(True):
            nombre = input("Ingrese nombre del contacto: ")
            telefono = input("Ingrese el numero de teléfono: ")
            flag = 0
            for name, cel in agenda.items():
                if nombre == name:
                    while True:
                        op = input(f"""
                        Nombre de contacto encontrado en la agenda
                        nombre: {name}
                        teléfono: {cel}                   
                        ¿Desea editarlo?
                        1. Si
                        2. No
                        """)
                        op = validarOpcionDos(op)
                        if op == 1:
                            nombre = input("Ingrese nuevo nombre de contacto: ")
                            telefono = input("Ingrese el nuevo numero de teléfono: ")
                            agenda[nombre]=telefono
                            flag = 1
                            break
                        if op == 2:
                            break
                if telefono == cel:
                    while True:
                        op = input(f"""
                        Numero de contacto encontrado en la agenda
                        nombre: {name}
                        telefono: {cel}                   
                        ¿Desea editarlo?
                        1. Si
                        2. No
                        """)
                        op = validarOpcionDos(op)
                        if op == 0:
                            continue
                        if op == 1:
                            nombre = input("Ingrese nuevo nombre de contacto: ")
                            telefono = input("Ingrese nuevo numero de telefono: ")
                            agenda[nombre]=telefono
                            flag = 1
                            break   
                        if op == 2:
                            break

            if flag == 0:
                agenda[nombre]=telefono

            while True:    
                op = input("""¿Desea agregar mas contactos?
                1. Si
                2. No
                """)
                op = validarOpcionDos(op)
                if op == 0:
                    continue
                if op == 1:
                    b = 1
                    break
                if op == 2:
                    b = 0
                    break
            if b == 0:
                op = 0
                break
            
                       
    if op == 2:
        while(True):
            buscar = input("Ingrese nombre o telefono a buscar: ")
            b = 0
            for name, cel in agenda.items():
                if buscar == name or buscar == cel:
                    print(f"""
                    Nombre: {name}
                    Teléfono: {cel}
                    """)
                    b = 1
            if b == 0:
                print("Contacto no encontrado")
            while True:
                op = input("""
                ¿Desea buscar algún contacto mas?
                1. Si
                2. No
                """)
                op = validarOpcionDos(op)
                if op == 0:
                    continue
                if op == 1:
                    b = 1
                    break
                if op == 2:
                    b = 0
                    break
            if b == 0:
                op = 0
                break
        
    if op == 3:
        while(True):
            delet = input("Ingrese el nombre o numero del contacto que desea eliminar: ")
            b = 0
            for name, cel in agenda.items():
                if delet == name or delet == cel:
                    op = input(f"Desea eliminar este contacto?\nNombre: {name} Teléfono: {cel} 1. Si\n2. No\n:")
                    validarOpcionDos(op)
                    b = 1
                else:
                    b = 0
            if b == 0:
                print("Contacto no encontrado")
            if b == 1:     
                if (op == 1):
                    agenda.pop(delet)
                elif(op == 2):
                    print("El contacto no sera borrado. Nuevamente...")
                
            while True:
                op = input("""
                ¿Desea eliminar algún contacto mas?
                1. Si
                2. No
                """)
                op = validarOpcionDos(op)
                if op == 0:
                    continue
                if op == 1:
                    b=1
                    break
                if op == 2:
                    b=0
                    break
            if b == 0:
                op = 0
                break

    if op == 4:
        while(True):
            for i, k in(agenda.items()):
                print(f"{i} : {k}")
            break

    if op == 5:
        break