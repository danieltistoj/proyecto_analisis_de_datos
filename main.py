import pynput.keyboard

def presiona(key):
    key1 = convertir(key)
    print("Tecla presionada: {}".format(key1))
def libera(key):
    key1 = convertir(key)
    print("Tecla liberada: {}".format(key1))
    if str(key) == "Key.esc":
        print("entro")
        print("saliendo...")
        return False
def convertir(key):
    if isinstance(key,pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

with pynput.keyboard.Listener(on_press=presiona,on_release=libera) as liste:
    liste.join()
