import platform
import psutil

print("HOLA MUNDO")
uname = platform.uname()

def get_size(bytes, suffix = 'B'):
    factor = 1024
    for unit in ["","K","M","G","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print("="*40, "SYSTEMA","="*40)
print(f"Systema: {uname.system}")
print(f"Nombre Host: {uname.node}")
print(f"Release: {uname.release}")
print(f"version: {uname.version}")
print(f"Machine:  {uname.machine}")
print(f"Procesador: {uname.processor}")

#Informacion de la CPU
print("="*40, "CPU INFO","="*40)
#No Nucleos
print("Nucleos Fisicos: ",psutil.cpu_count(logical=False))
print("Total Nucleos: ",psutil.cpu_count(logical=True))
#Frecuencia CPU
freq = psutil.cpu_freq()
print(f"frecuencia MAX: {freq.max:.2f}Mhz")
print(f"frecuencia MIN: {freq.min:.2f}Mhz")
print(f"Frecuencia Actual: {freq.current:.2f}Mhz")
#USO DE CPU
print("Uso CPU por Nucleo")
for i, percentage in enumerate (psutil.cpu_percent(percpu=True)):
    print (f"Core {i} : {percentage}%")
print (f"Total uso CPU: {psutil.cpu_percent()}%")

#MEMORIA
print("="*40, "Informacion de Memoria", "="*40)
vm = psutil.virtual_memory()
print(f"Total: {get_size(vm.total)}")
print(f"Disponible: {get_size(vm.available)}")
print(f"En Uso: {get_size(vm.used)}")
print(f"porcentaje: {get_size(vm.percent)}%")
print("="*40, "SWAP", "="*40)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Libre: {get_size(swap.free)}")
print(f"En Uso: {get_size(swap.used)}")
print(f"porcentaje: {get_size(swap.percent)}%")

#Informacion Disco Duro

print("="*40,"Informacion Disco Duro","="*40)
print("Particion y Uso:")
particiones = psutil.disk_partitions()
for particion in particiones:
    print (f"==== Dispositivo : {particion.device} ====")
    print (f"MountPoint : {particion.mountpoint} ")
    print (f"File System Type : {particion.fstype} ")
    try:
        uso = psutil.disk_usage(particion.mountpoint)
    except PermissionError:
        continue
    print(f" Tamaño: {get_size(uso.total)}")
    print(f" en Uso: {get_size(uso.used)}")
    print(f" Libre: {get_size(uso.free)}")
    print(f" Porcentaje: {get_size(uso.percent)}%")

disk_io = psutil.disk_io_counters()
print(f"Lectura Total : {get_size(disk_io.read_bytes)}")
print(f"Escritura Total : {get_size(disk_io.write_bytes)}")

#Informacion de Red
print("="*40,"Informacion de Red", "="*40)
addrs = psutil.net_if_addrs()
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
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size (net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size (net_io.bytes_recv)}")





