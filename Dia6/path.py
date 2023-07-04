from pathlib import Path

#Construir objetos que corresponden a una ruta de acceso
#Instancia path con ruta absoluta al directorio principal del usuario actual
base=Path.home()
#Ruta relativa, no absoluta
guia=Path(base,'Europa','España',Path('Barcelona','Sagrada_Familia.txt'))


#print(base)
print(guia)
#Devuelve el antecesor de una ruta de archivos determinada
print(guia.parent)
print(guia.parent.parent)

guia2=guia.with_name('La_Pedrera.txt')

print(guia2)