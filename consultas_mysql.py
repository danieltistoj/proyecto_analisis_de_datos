from h5py.h5pl import insert

import mysql

db = mysql.BasedeDatos()

def existe_equipo(ip):
    query = "SELECT id FROM equipo WHERE ip ='"+ip+"'"
    try:
        id = -1
        db.cursor.execute(query)
        datos = db.cursor.fetchall()
        for dato in datos:
            id = dato

        if id>0:
            return id
        else:
            insertar_equipo(ip) #Inserta el equipo en la base de datos
            return obtener_ultimo_id("equipo")
    except:
        print("Errro consulta existe equipo")

def obtener_ultimo_id(tabla):
    query = "SELECT MAX(id) FROM {}".format(tabla)
    try:
        db.cursor.execute(query)
        dato = db.cursor.fetchall()
        print(dato)
        return dato
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
    pass


