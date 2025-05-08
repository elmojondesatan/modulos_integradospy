#modules
from programas.sumas import sumar2
from programas.restas import restar2
from programas.menu import menu
from vistas.lineas import lineas_cantidad
from datetime import datetime

#Modulos de python
import os



while(True):
    os.system("clear")
    print("Hora: ",datetime.now().strftime("%H:%H:%S"))

programa = True
while(programa):
    lineas_cantidad(40)
    menu()
    res = int(input("|[?]: "))

    if res == 1:
        print("Suma dos numeros")

        sumar2()
        
    elif res == 2:
        print("Restar dos numeros")
        restar2()

    elif res == 0:
        print("Salir del programa")
        programa = False


os.system("clear")

