import platform

print("HOLA MUNDO")
uname = platform.uname()

print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"version: {uname.version}")
print(f"Machine:  {uname.machine}")
print(f"Processor: {uname.processor}")