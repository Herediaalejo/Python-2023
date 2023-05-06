def recordatorio(mes="Enero", nro="1", dia = "lunes"):
    recordatorios=[]
    fin = False
    op = 0
    while fin==False:
        tarea = input(f"¿Que desea recordar el dia {dia} {nro} de {mes}?\n")
        recordatorios.append([ "dia: " + dia , "nro: " + nro , "mes: " + mes , "tarea: " +tarea])
        op = int(input("""¿Desea registrar algo mas?
        1)Si
        2)No
        """))
        if(op==1):
            dia = input("¿Que dia?\n")
            nro = input("¿Que número?\n")
            mes = input("¿Que mes?\n")
        elif(op==2):
            fin=True
    print(recordatorios)
recordatorio("Mayo", "2")