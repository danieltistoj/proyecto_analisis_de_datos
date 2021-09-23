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

def insertar_InfoSistema(id_ejecucion,diccionario):
    query = "INSERT INTO informacion_del_sistema(systema,nombre,release_,version,machine,procesador,id_ejecucion)  VALUES('{}','{}','{}','{}','{}','{}',{})".format(diccionario['Systema'],diccionario['Nombre Host'],diccionario['Release'],diccionario['Version'],diccionario['Machine'],diccionario['Procesador'],id_ejecucion)
    try:
        print(query)
        db.cursor.execute(query)
    except:
        print("Error al insertar proceso")
#insertar_ejecucion("","","192.168.191.82")

def insertar_InfoCPU(id_ejecucion,diccionario):
    
    query = "INSERT INTO informacion_cpu(nucleos_fisicos,procesadores,frecuencia_max,frecuencia_min,frecuencia_actual,total_nucleos,id_ejecucion)  VALUES('{}','{}','{}','{}','{}','{}',{})".format(diccionario['Nucleos Fisicos'],diccionario['Procesadores Logicos'],diccionario['Frecuencia MAX'],diccionario['Frecuencia MIN'],diccionario['Frecuencia actual'],diccionario['Total Uso Nucleos'],id_ejecucion)
    try:
        print(query)
        db.cursor.execute(query)
    except:
        print("Error al insertar proceso")
    id = obtener_ultimo_id("informacion_cpu")
    nucleos = diccionario['Uso de Nucleos'] 
    insertar_Nucleos(id,nucleos)
    

def insertar_Nucleos(id,diccionario):
    for key in diccionario:
        query =   "INSERT INTO uso_nucleos(core,porcentaje,id_informacion_cpu)  VALUES('{}','{}',{})".format(key,diccionario[key],id)
        try:
            print(query)
            db.cursor.execute(query)
        except:
            print("Error al insertar proceso")

def insertar_InfoMemoria(id_ejecucion,diccionario):
    query = "INSERT INTO informacion_memoria(total,disponible,en_uso,porcentaje,id_ejecucion)  VALUES('{}','{}','{}','{}',{})".format(diccionario['Total'],diccionario['Disponible'],diccionario['En uso'],diccionario['Porcentaje'],id_ejecucion)
    try:
        print(query)
        db.cursor.execute(query)
    except:
        print("Error al insertar proceso")

def insertar_InfoSWAP(id_ejecucion,diccionario):
    query = "INSERT INTO swap(total,libre,en_uso,porcentaje,id_ejecucion)  VALUES('{}','{}','{}','{}',{})".format(diccionario['Total'],diccionario['Libre'],diccionario['En uso'],diccionario['Porcentaje'],id_ejecucion)
    try:
        print(query)
        db.cursor.execute(query)
    except:
        print("Error al insertar proceso")

def insertar_InfoDiscoDuro(id_ejecucion,diccionario): 
    query = "INSERT INTO disco_duro(lectura_total,escritura_total,id_ejecucion)  VALUES('{}','{}',{})".format(diccionario['Lectura Total'],diccionario['Escritura Total'],id_ejecucion)
    try:
        print(query)
        db.cursor.execute(query)
    except:
        print("Error al insertar proceso")
    id = obtener_ultimo_id("disco_duro")
    for key in diccionario:
        if key == "Lectura Total":
            print("Se encontro una lectura total")
        elif key == "Escritura Total":
            print("Se encontro una Escritura total")
        else:
            particion = diccionario[key]
            query =  "INSERT INTO particion(particion,dispositivo,mountPoint,file_system,tamano,en_uso,libre,id_disco_duro)  VALUES('{}','{}\\','{}\\','{}','{}','{}','{}',{})".format(key,particion['Dispositivo'],particion['MountPoint'],particion['File System Type'],particion['Tamaño'],particion['En Uso'],particion['Libre'],id)
            try:
                print(query)
                db.cursor.execute(query)
            except:
                print("Error al insertar proceso")

def insertar_InfoRedes(id_ejecucion,diccionario): 
    query = "INSERT INTO informacion_red(total_bytes_enviados,total_byte_received,id_ejecucion)  VALUES('{}','{}',{})".format(diccionario['Total Bytes enviados'],diccionario['Total Bytes Received'],id_ejecucion)
    try:
        print(query)
        db.cursor.execute(query)
    except:
        print("Error al insertar proceso")



