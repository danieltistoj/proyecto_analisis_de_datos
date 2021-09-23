from mongobd import conexion
import matplotlib.pylab as plt


class grafica:
    def __init__(self):
        self.con = conexion()
    def grafica_barras(self):
        #Muestra el nuemero de ejecuciones de cada maquina en una grafica de barras
        ips, res = self.con.agregacion()
        plt.bar(ips, res)
        plt.show()
        plt.close('all')


graf = grafica()
graf.grafica_barras()


