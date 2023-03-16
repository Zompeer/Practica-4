def ordena(arr, registro):
    n = len(arr)
    # Recorre todos los elementos del arreglo
    for i in range(n):
        # La última i elementos ya están en su lugar correcto
        for j in range(i+1, n):
            # Compara elementos adyacentes
            if int(arr[j][registro]) < int(arr[i][registro]):
                # Intercambia los elementos si el anterior es mayor que el siguiente
                arr[i], arr[j] = arr[j], arr[i]
def mostrar(arreglo):
    for registro in arreglo:
        print(registro)
def FIFO(procesos, SEPARADOR):
    print("SJF")
    tiempo = 0
    ordenEjecucion = list()
    ordena(procesos, 1)
    print(SEPARADOR)
    print("Procesos ordenados")
    mostrar(procesos)

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
                procesos[0][1] = str(int(procesos[0][1])-1)
        else:
            print("Ejecutando "+str(procesos[0]))
            procesos[0][1] = str(int(procesos[0][1])-1)
    print("\nOrden de finalizacion")
    return ordenEjecucion