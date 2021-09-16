#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
# Comprobamos que existen las librerías necesarias
# python-mysqldb
try:
    import MySQLdb
except ImportError:
    print ("No se encuentra la biblioteca MySQLdb")
    exit()
import smtplib
from email.mime.text import MIMEText
# python-lxml
try:
    from lxml import etree
except ImportError:
    print ("No se encuentra la biblioteca lxml")
    exit()    
from ConfigParser import SafeConfigParser
from getpass import getpass

# Cargamos en parser el fichero de configuración
parser = SafeConfigParser()
parser.read('infohardware.cfg')

# Realizamos la conexión a la Base de Datos
# Versión IESGN: Se pide contraseña por teclado, si no es correcta termina.
try:
    db = MySQLdb.connect(host = parser.get('mysql','host'),
                         user = parser.get('mysql','user'),
                         passwd = getpass("Contraseña de MySQL: "),
                         db = parser.get('mysql','db'))
except:
    exit()
cursor = db.cursor()

# Versión IESGN: Función que busca el número de serie siguiente para los
# equipos que no tienen número de serie asignados.
def buscar_ns_iesgn():
    sql = "select num_serie from equipo where num_serie like 'iesgn%' \
order by num_serie desc"
    cursor.execute(sql)
    tupla = cursor.fetchone()
    if tupla != None:
        return "%.4d" % ((int)(tupla[0][5:]) + 1)
    else:
        return "0001"

def conversor(cant, columna):
    """
    Función para convertir el tamaño de los discos duros a MB/GB y las
    frecuencias de las memorias RAM a MHz.
    Recibe la cantidad en bytes o Hz y devuelve una cadena que expresa
    la misma cantidad en MB o GB (discos duros) o MHz (ram)
    """
    aux = cant
    if columna == "size" and aux != "":
        unit = ['MB','GB']
        aux = int(cant) / 2**20
        if aux >= 1024:
            aux = "%s %s" % (str(aux / 1024), unit[1])
        else:
            aux = str(aux) + unit[0]
    if columna == "clock" and aux != "":
        aux = "%d MHz" % (int(cant) / 10**6)
    return aux

def obtener_datos(arbol, ruta, datos, adicionales = None):
    """
    Función que lee del arbol xml donde tenemos la configuración del 
    equipo los datos que le indicamos a partir de una expresión xpath.
    Devuelve los datos leidos del arbol xml además de los datos que 
    opcionalmente se pueden pasar en el parámetro adicionales.

    arbol - Objeto ElementTree que representa la información del sistema
    ruta - Expresión xpath base para realizar la consultas
    datos - Lista donde se guarda los datos que vamos a leer
    adicionales - Lista opcional donde guardamos datos que se van a 
    devolver, además de los datos leídos con xpath

    La función devuelve una lista con los datos leidos (diccionario) 
    haciendo las consultas con xpath más los posibles datos que se 
    han recibido en el parámetro adicionales.
    """
    respuesta = []
   
    # Calculamos el número de datos que vamos a consultar con xpath
    # Si hemos enviado datos adicionales, será el tamaño de la lista 
    # datos menos la longitud de la lista adicionales.
    if adicionales != None:
        cantcolxml = len(datos) - len(adicionales)
    else:
        cantcolxml = len(datos)
    
    # Comprobamos el número de componentes (cantidad de discos duros,
    # cantidad de memorias, ...
    num_componentes = int(arbol.xpath('count(%s)' % ruta))
    for i in xrange(num_componentes):
        intermedio = {}
        cont_adicionales = 0
        cont_datos = 1
        # Para cada dato lo intnetamos leer del arbol xml con la expresión xpath
        # sino es posible, si todavía estamos leyendo datos con xpath, el valor
        # es cadena vacia, si ya hemos leido toddos los datos con xpath, el valor
        # se obtendra de la lista adicionales. 
        for dato in datos:
            try:
                valor = arbol.xpath("%s/%s/text()" % (ruta,dato))[i]
            except:
                if cont_datos <= cantcolxml:
                    valor = ""
                else:
                    if adicionales != None:
                        valor = adicionales[cont_adicionales]
                        cont_adicionales += 1
            intermedio[dato] = valor
            cont_datos += 1
        respuesta.append(intermedio)
    return respuesta

