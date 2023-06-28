#Generar numeros aleatorios
#importar metodos a python

from random import *

aleatorio=randint(1,50)
print(aleatorio)

aleatorio2=round(uniform(1,5),1)
print(aleatorio2)

#Entre 0 y 1
aleatorio3=random()
print(aleatorio3)

#aleatorio de una lista
colores=['azul','rojo','verde','amarillo']
aleatorio4=choice(colores)
print(aleatorio4)

numeros=list(range(5,50,5))
shuffle(numeros)
print(numeros)
