import wmi
def ultimos_procesos():
    f = wmi.WMI()
    procesos = ""
    print("pid   Process name")

    for process in f.Win32_Process():
       procesos = procesos  +  f"{process.ProcessId:<10} {process.Name}"+"\n"
    return procesos
#https://es.acervolima.com/2021/02/09/python-obtener-una-lista-de-los-procesos-en-ejecucion/