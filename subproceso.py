from builtins import map
import consultas_mysql
import wmi
consulta = consultas_mysql
def ultimos_procesos():
    diccionario ={}
    f = wmi.WMI()

    procesos = ""
    #print("pid   Process name")
    size = len(f.Win32_Process())
    print(size)
    for process in f.Win32_Process():
        diccionario[f"{process.ProcessId}"] = f" {process.Name}"
    return diccionario

def ultimos_procesos_matriz(id_ejecucion):

    f = wmi.WMI()
    # print("pid   Process name")
    size = len(f.Win32_Process())
    print(size)
    for process in f.Win32_Process():
        id = f"{process.ProcessId}"
        nombre = f" {process.Name}"

        consulta.insertar_proceso(id,nombre,id_ejecucion)




#https://es.acervolima.com/2021/02/09/python-obtener-una-lista-de-los-procesos-en-ejecucion/