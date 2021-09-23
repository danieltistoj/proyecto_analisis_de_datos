from mongobd import conexion
import matplotlib.pylab as plt
from mysql import BasedeDatos



class grafica:
    def __init__(self):
        self.con = conexion()
        self.con_mysql = BasedeDatos()
    def grafica_barras(self):
        #Muestra el nuemero de ejecuciones de cada maquina en una grafica de barras
        ips, res = self.con.agregacion_ip()

        plt.bar(ips, res)
        plt.title("Ejecuciones por equipo MongoDB")
        plt.xlabel("Nombre de Host")
        plt.ylabel("Numero de ejecuciones")
        plt.show()
        plt.close('all')


    def grafica_barras_mysql(self):
        query = "SELECT nombre, COUNT(*) FROM informacion_del_sistema GROUP BY nombre HAVING nombre != '2'"

        nombres = []
        num_ejecuciones =[]
        self.con_mysql.cursor.execute(query)

        while True:
            dato = self.con_mysql.cursor.fetchone()
            if dato == None:
                break
            nombres.append(dato[0])
            num_ejecuciones.append(dato[1])

        plt.bar(nombres,num_ejecuciones)
        plt.title("Ejecuciones por equipo MySQL")
        plt.xlabel("Nombre del equipos")
        plt.ylabel("Numero de ejecuciones")
        plt.show()
        plt.close('all')




