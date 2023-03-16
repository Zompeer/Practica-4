def RR(procesos, quantum , SEPARADOR):
    print("Round Robin (Quantum 3)")
    expiracion = quantum
    tiempo = 0
    ordenEjecucion = list()

    while(True):
        if not procesos:
            break
        print(SEPARADOR)
        print("Tiempo: "+str(tiempo))
        print(SEPARADOR)
        tiempo+=1
        if int(procesos[0][1]) == 0:
            print("Ejecucion Finalizada "+str(procesos[0]))
            ordenEjecucion.append(procesos[0])
            procesos.pop(0)
            if procesos:
                print("Ejecutando "+str(procesos[0]))
                expiracion = quantum-1
                procesos[0][1] = str(int(procesos[0][1])-1)
            else:
                expiracion = -1
        else:
            if expiracion == 0:
                print("Expiró "+str(procesos[0]))
                procesos.append(procesos[0])
                procesos.pop(0)
                expiracion = quantum-1
            else:
                expiracion-=1
            print("Ejecutando "+str(procesos[0]))
            procesos[0][1] = str(int(procesos[0][1])-1)
    print("\nOrden de finalizacion")
    return ordenEjecucion