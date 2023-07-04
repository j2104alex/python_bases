from pathlib import Path,PureWindowsPath

carpeta=Path('C:/Users/HP/Desktop/programacion/PRACTICA/Python/Dia6/prueba.txt')

ruta_windows=PureWindowsPath(carpeta)
#Leer un archivo
print(carpeta.read_text())
#nombre
print(carpeta.name)
#tipo
print(carpeta.suffix)
#nombre sin terminacion
print(carpeta.stem)

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Genial,existe')

print(ruta_windows)