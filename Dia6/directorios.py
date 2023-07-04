import os

#obtener el directorio de trabajo actual
ruta=os.getcwd()
#cambiar de directorio, ruta diferente de trabajo
ruta2=os.chdir('C:\\Users\\HP\\Desktop\\programacion\\PRACTICA\\Python\\alternativo')
#crear carpetas
#ruta3=os.makedirs('C:\\Users\\HP\\Desktop\\programacion\\PRACTICA\\Python\\alternativo\\otra')
archivo=open('otro_archivo.txt')
print(archivo.read())
print(ruta,ruta2)

ruta4='C:\\Users\\HP\\Desktop\\programacion\\PRACTICA\\Python\\Dia6\\prueba.txt'

nombre_elemento=os.path.basename(ruta4)
base_elemento=os.path.dirname(ruta4)
tupla_nombre_base=os.path.split(ruta4)

print('************')
print('Aca: '+nombre_elemento,base_elemento)
print(tupla_nombre_base)

#Borrar una carpeta
#os.rmdir('C:\\Users\\HP\\Desktop\\programacion\\PRACTICA\\Python\\alternativo\\otra')


otro_archivo=open('C:\\Users\\HP\\Desktop\\programacion\\PRACTICA\\Python\\alternativo\\otro_archivo.txt')

print(otro_archivo.read())