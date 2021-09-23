from mongobd import conexion
import matplotlib.pylab as plt



class grafica:
    def __init__(self):
        self.con = conexion()
    def grafica_barras(self):
        #Muestra el nuemero de ejecuciones de cada maquina en una grafica de barras
        ips, res = self.con.agregacion_ip()

        plt.bar(ips, res)
        plt.title("Ejecuciones por equipo")
        plt.xlabel("IP de equipos")
        plt.ylabel("Numero de ejecuciones")
        plt.show()
        plt.close('all')
    def grafica_concurrencia(self):
        fecha_hora, res = self.con.agregacion_concurrencia()


graf = grafica()
graf.grafica_barras()


