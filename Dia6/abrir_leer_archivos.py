#E-S/IO: Entrada/salida Input/Output
'''Cuando se abre el archivo para solo lectura
se coloca mi_archivo=open('prueba.txt','r')
si no se pone el argumento python dedude que es solo
lectura'''

#Abrir
mi_archivo=open('prueba.txt')
print(mi_archivo)
#Leer
#print(mi_archivo.read())
print('*********')

#una_linea=mi_archivo.readline()
#En el archivo tiene un salto de linea al final, para quitarla rstrip()
#print(una_linea.rstrip())
#una_linea=mi_archivo.readline()
#print(una_linea)
#una_linea=mi_archivo.readline()
#print(una_linea)
#mi_archivo.close()

'''for line in mi_archivo:
    print('Aquí dice: '+line)'''

#Queda como una lista
'''todas_lineas=mi_archivo.readlines()
todas_lineas=todas_lineas.pop()
print(todas_lineas)'''

lineas=mi_archivo.readlines()

print(lineas[1])