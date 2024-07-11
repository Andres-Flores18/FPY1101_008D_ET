import csv
import random
import os
import time
clear=("cls")

sueldo=random.randint(300000, 2500000)

def registro():
    nombre=input("ingresa nombre")
    sueldo
    salud=round(sueldo*0.7)
    afp=round(sueldo*0.12)
    liquido=(sueldo - salud- afp)
    return(nombre, sueldo, salud, afp,liquido)

def trabajadores1(nombre, sueldo,salud,afp,liquido, archivo_csv= 'trabajadores.csv'):
    with open(archivo_csv, 'a', newline='') as archivo:
        campo=['nombre', 'sueldo','descuento salud','descuento afp','liquido']
        escritor_csv=csv.DictWriter(archivo, fieldnames=campo)
        if archivo.tell()==0:
         escritor_csv.writeheader()
        
        escritor_csv.writerow({
           'nombre':nombre,
           'sueldo':sueldo,
           'descuento salud':salud,
           'descuento afp':afp,
           'liquido':liquido
        })

def mostrar(archivo_csv='trabajadores.csv'):
    with open(archivo_csv,'r', newline='')as archivo:
        lector=csv.reader(archivo)
        next(lector)
        for fila in lector:
         print(f"nombre empleado: {fila[0]},"f"sueldo base: {fila[1]},"f"descuento salud: {fila[2]},"f"descuento afp:{fila[3]}")

def menu():
    while True:
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldo")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldo")
        print("5. Salir del programa")
        opc=int(input("ingresa una opcion del 1 al 5:"))
        if opc==1:
            time.sleep(2)
            os.system("cls")
            nombre,sueldo,salud,afp,liquido=registro()
            trabajadores1(nombre,sueldo,salud,afp,liquido)
            time.sleep(2)
            os.system("cls")
        elif opc==2:
           time.sleep(2)
           os.system("cls")
           print("clasificando sueldo")

        elif opc==3:
           time.sleep(2)
           os.system("cls")
           print("estadisticas")
           
        elif opc==4:
           time.sleep(2)
           os.system("cls")
           mostrar()
           print("*"*150)
        elif opc==5:
           time.sleep(2)
           os.system("cls")
           print("Finalizando progama...")
           print("Desarrollado por: Andres Flores")
           print("RUT 21.643.265-7")
           break
menu()


