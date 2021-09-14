import wmi

f = wmi.WMI()

print("pid   Process name")

for process in f.Win32_Process():
    print(f"{process.ProcessId:<10} {process.Name}")
#https://es.acervolima.com/2021/02/09/python-obtener-una-lista-de-los-procesos-en-ejecucion/