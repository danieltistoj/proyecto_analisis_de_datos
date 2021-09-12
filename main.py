import pynput.keyboard
#trabajar con palabras
lista_tecla=[] #En esta lista se guardaran las palabras
def imprimir():
    tecla = ''.join(lista_tecla)
    print(tecla)

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
