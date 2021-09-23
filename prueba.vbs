Set WshShell = WScript.CreateObject("WScript.Shell")
obj = WshShell.Run("""C:\Users\Usuario\Desktop\Proyecto Analisis de datos\Archivo.cmd""", 0)
set WshShell = Nothing