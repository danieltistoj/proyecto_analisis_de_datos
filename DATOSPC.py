import platform
import psutil
import wmi

print("HOLA MUNDO")
uname = platform.uname()

def get_size(bytes, suffix = 'B'):
    factor = 1024
    for unit in ["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def informacion_sistema():
    diccionario = {'Systema' : uname.system,
                   'Nombre Host' : uname.node,
                   'Release' : uname.release,
                   'Version' : uname.version,
                   'Machine' : uname.machine,
                   'Procesador' : uname.processor}
    return diccionario 

def informacion_CPU():
    freq = psutil.cpu_freq()
    nucleos = {}
    for i, percentage in enumerate (psutil.cpu_percent(percpu=True)):
        nucleoI = {f"Core {i}" : f"{percentage}%"}
        nucleos.update(nucleoI)
    diccionario = {'Nucleos Fisicos' : psutil.cpu_count(logical=False),
                   'Procesadores Logicos' : psutil.cpu_count(logical=True),
                   'Frecuencia MAX' : f"{freq.max:.2f} Mhz",
                   'Frecuencia MIN' : f"{freq.min:.2f}Mhz",
                   'Frecuencia actual' : f"{freq.current:.2f} Mhz",
                   'Uso de Nucleos' : nucleos,
                   'Total Uso Nucleos' : f"{psutil.cpu_percent()} %"
                  }
    return diccionario 

def informacion_Memoria():
    vm = psutil.virtual_memory()
    diccionario = {'Total' : get_size(vm.total),
                   'Disponible' : get_size(vm.available),
                   'En uso' : get_size(vm.used),
                   'Porcentaje' : f"{get_size(vm.percent)} %",
                  }
    return diccionario 

def informacion_MemoriaSWAP():
    swap = psutil.swap_memory()
    diccionario = {'Total' : get_size(swap.total),
                   'Libre' : get_size(swap.free),
                   'En uso' : get_size(swap.used),
                   'Porcentaje' : f"{get_size(swap.percent)}%"
                  }
    return diccionario

def Disco_Duro():
    swap = psutil.swap_memory()
    particiones = psutil.disk_partitions()
    i = 0
    InfoParticiones = {}
    disk_io = psutil.disk_io_counters()
    for particion in particiones:
        i = i+1
        uso = psutil.disk_usage(particion.mountpoint)
        infoi = {'Dispositivo' : particion.device,
                 'MountPoint' :  particion.mountpoint,
                 'File System Type' : particion.fstype,
                 'Tamaño' :  get_size(uso.total),
                 'En Uso' : get_size(uso.used),
                 'Libre' : get_size(uso.free),
                 'Porcentaje' : f"{get_size(uso.percent)}%"
                }   
        particioni = {f"Particion {i} " : infoi}
        InfoParticiones.update(particioni)
    infoGeneral = {'Lectura Total' : get_size(disk_io.read_bytes),
                   'Escritura Total' : get_size(disk_io.write_bytes)}
    InfoParticiones.update(infoGeneral)
    return InfoParticiones

def infoRED():
    addrs = psutil.net_if_addrs()
    redes = {}
    redi = {}
    redgeneral = {} 
    x =0
    for interface_name, interface_addresses in addrs.items():
        x = x+1
        print(x)
        for address in interface_addresses:
            if str(address.family)=='AddressFamily.AF_INET':
                redgeneral = {'IP Address' : address.address,
                              'Netmask' : address.netmask ,
                              'Broadcast IP' : address.broadcast}
            elif str(address.family)=='AddressFamily.AF_PACKET':
                redgeneral = {'MAC Address' : address.address,
                              'Netmask' : address.netmask ,
                              'Broadcast MAC' : address.broadcast}
            redi = {f"{interface_name}" : redgeneral}
            redes.update(redi)
    net_io = psutil.net_io_counters()
    redgeneral = {'Total Bytes enviados' : get_size(net_io.bytes_sent),
                  'Total Bytes Received' : get_size (net_io.bytes_recv)}
    redes.update(redgeneral)
    return redes


"""Informacion de Red
print("="*40,"Informacion de Red", "="*40)
for interface_name, interface_addresses in addrs.items():
    for address in interface_addresses:
        print(f"==== Interface: {interface_name}====")
        if str(address.family)=='AddressFamily.AF_INET':
            print(f" IP Address: {address.address}")
            print(f" Netmask: {address.netmask}")
            print(f" Broadcast IP: {address.broadcast}")
        elif str(address.family)=='AddressFamily.AF_PACKET':
            print(f" MAC Address: {address.adress}")
            print(f" Netmask: {address.netmask}")
            print(f" Broadcast MAC: {address.broadcast}")

print(f"Total Bytes Sent: {get_size (net_io.bytes_sent)}")
print(f"Total Bytes Received: {)}")
"""