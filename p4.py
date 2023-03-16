import os
from RoundRobin import *
from SJF import *
from FIFO import *
from Prioridad import *
CLEAR = "cls"
def separar(a_separar, separador):
    arreglo = list()
    registro = ""
    for letra in a_separar:
        if letra == separador or letra == '\n':
            arreglo.append(registro)
            registro = ""
            continue
        registro += letra
    if letra != "\n":
        arreglo.append(registro)
    return arreglo
def mostrar(arreglo):
    for registro in arreglo:
        print(registro)
debug = True
def deb(texto):
    global debug
    if debug:
        print(texto)
archivo = open("procesos.txt", "r")
separacion = archivo.readlines()
procesos = list()
for registro in separacion:
    procesos.append(separar(registro,","))
print("Procesos de entrada")
SEPARADOR = "----------------------------------------------"

def crearProceso():
    proceso = list()
    while(True):
        proceso.append(input("Nombre de proceso: "))
        try:
            proceso.append(str(int(input("Tiempo de proceso: "))))
            proceso.append(str(int(input("Prioridad de proceso: "))))
        except:
            print("Algo fallo en los datos introducidos")
            continue
        return proceso
SEPARADOR = "------------------------------------"


while(True):
    print(SEPARADOR)
    mostrar(procesos)
    print(SEPARADOR)
    print("")
    print("1) Insertar nuevo proceso al inicio")
    print("2) Agregar nuevo proceso al final")
    print("3) Ejecutar procesos")
    try:
        opc = int(input("Elige opcion: "))
    except:
        print("Elige una opcion válida")
        os.system(CLEAR)
        continue
    if opc == 1:
        nvoProceso = crearProceso()
        procesos.insert(0, nvoProceso)
    elif opc == 2:
        nvoProceso = crearProceso()
        procesos.append(nvoProceso)
    elif opc == 3:
        print(SEPARADOR)
        print("1) Round Robin")
        print("2) FIFO")
        print("3) SJF")
        print("4) Prioridad")
        try:
            opc2 = int(input("Elige opcion: "))
        except:
            print("Opcion no válida")
            os.system(CLEAR)
            continue
        if opc2 == 1:
            try:
                quantum = int(input("Elige el quantum: "))
                if quantum < 1:
                    raise Exception("El quantum no puede ser menor que 1")
                mostrar(RR(procesos, 3 ,SEPARADOR))
            except:
                print("Ingreso un valor erroneo")
            
        elif opc2 == 2:
            mostrar(FIFO(procesos, SEPARADOR))
        elif opc2 == 3:
            mostrar(SJF(procesos, SEPARADOR))
        elif opc2 == 4:
            mostrar(PRIORIDAD(procesos, SEPARADOR))
        else:
            print("Elige una opcion válida")
    else:
        print("Elige una opcion válida")
    f = input("Ingresa s o S para continuar: ")
    if f == "s" or f == "S":
        os.system(CLEAR)
        if opc== 3:
            for registro in separacion:
                procesos.append(separar(registro,","))
        continue
    else:
        break