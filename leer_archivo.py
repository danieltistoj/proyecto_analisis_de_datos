equipo = ""
fecha_hora = ""
informacion = ""
contador = 0
with open("log.txt","r") as archivo:
    for linea in archivo:
        if contador == 0:
            equipo = linea
        elif contador == 1:
            fecha_hora = linea
        else:
            informacion = informacion + linea
        contador = contador+1

print("equipo: "+equipo)
print("fecha y hora: "+fecha_hora)
print("informacion: "+informacion)