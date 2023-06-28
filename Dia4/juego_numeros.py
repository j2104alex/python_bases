from random import *

aleatorio=randint(1,100)
intentos=8

nombre=input('Dime tu nombre: ')
numero=int(input(f'Bueno {nombre} trata de adivinar el número, está en un rango de 1 a 100. \nTienes 8 intentos, mucha suerte: '))
while intentos >= 0:
    if numero<aleatorio:
        numero = int(input('Ingrese un número mayor: '))
        intentos-=1
    elif numero > aleatorio:
        numero = int(input('Ingrese un número menor: '))
        intentos -= 1

    else:
        print(f'Has adivinado el número, te quedaron {intentos} intentos')
        break

else:
    print(f'No tienes mas intentos, lo siento, el número secreto era {aleatorio}')

