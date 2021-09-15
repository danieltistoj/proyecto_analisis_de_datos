import wmi
def ultimos_procesos():
    diccionario ={}
    f = wmi.WMI()
    procesos = ""
    #print("pid   Process name")

    for process in f.Win32_Process():
        diccionario[f"{process.ProcessId}"] = f" {process.Name}"
    return diccionario

#https://es.acervolima.com/2021/02/09/python-obtener-una-lista-de-los-procesos-en-ejecucion/