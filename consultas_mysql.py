from h5py.h5pl import insert

import mysql

db = mysql.BasedeDatos()

def existe_equipo(ip):
    query = "SELECT id FROM equipo WHERE ip ='"+ip+"'"
    try:
        id = -1
        db.cursor.execute(query)
        while True:
            fila = db.cursor.fetchone()
            if fila == None:
                break
            id = fila[0]


        if id>0:
            print("se encontro la id: {}".format(id))
            return id
        else:
            insertar_equipo(ip) #Inserta el equipo en la base de datos
            return obtener_ultimo_id("equipo")
    except:
        print("Error consulta existe equipo")

def obtener_ultimo_id(tabla):
    query = "SELECT MAX(id) FROM {}".format(tabla)
    try:
        db.cursor.execute(query)
        dato = db.cursor.fetchone()
        print(dato[0])
        return dato[0]
    except:
        print("Error al buscar ultimo id")

def insertar_equipo(ip):
    query = "INSERT INTO equipo(ip) VALUES('"+ip+"')"
    try:
        db.cursor.execute(query)
        print("Se inserto el equipo: "+ip)
    except:
        print("Error al insertar equipo")

def insertar_ejecucion(tiempo_inicial,tiempo_final,ip):
    id_equipo = existe_equipo(ip)
    query = "INSERT INTO ejecucion(fecha_hora_inicio,fecha_hora_final,id_equipo) VALUES('{}','{}','{}')".format(tiempo_inicial,tiempo_final,id_equipo)
    try:
        db.cursor.execute(query)
        print("Insertar ejecucion correctamente")
    except:
        print("Error al insertar ejecucion")

def mostrar_equipos():
    query = "SELECT * FROM equipo"
    db.cursor.execute(query)
    while(True):
        row = db.cursor.fetchone()
        if row == None:
            break
        print(row[0])

def insertar_proceso(ip,nombre,id_ejecucion):
    query = "INSERT INTO proceso(ip,nombre,id_ejecucion) VALUES('{}','{}',{})".format(ip,nombre,id_ejecucion)
    try:
        print(query)
        db.cursor.execute(query)
    except:
        print("Error al insertar proceso")


#insertar_ejecucion("","","192.168.191.82")
