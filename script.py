import os

ruta = "C:/Users/ironm/Music/trabajos/renombrar-archivos"

if not os.path.exists(ruta):
    print("La carpeta no existe")
else:
    for i, archivo in enumerate(os.listdir(ruta)):
        nombre, extension = os.path.splitext(archivo)
        nuevo_nombre = f"archivo_{i}{extension}"
        
        os.rename(f"{ruta}/{archivo}", f"{ruta}/{nuevo_nombre}")

    print("Archivos renombrados correctamente")