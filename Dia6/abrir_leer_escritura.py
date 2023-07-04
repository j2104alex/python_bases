'''
mi_archivo=open('prueba.txt','w') Solo escritura
mi_archivo=open('prueba.txt','a') Solo escritura al final del archivo
                                  Si no existe lo crea
'''

archivo=open('prueba1.txt','w')

#Escribir linea
archivo.write('Soy el nuevo texto \nHola mundo!')

#Escribir lista de strings (strings uno detras del otro)
archivo2=open('prueba2.txt','w')
#Imprime esto= Holamundoaquíestoy
archivo2.writelines(['Hola','mundo','aquí','estoy'])

lista=['Hola','mundo','aquí','estoy']

for line in lista:
    archivo2.writelines(line+'\n')

archivo3=open('prueba3.txt','a')

archivo3.write('\nBienvenidos')


archivo.close()