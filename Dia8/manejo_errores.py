def suma():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    print(n1 + n2)
    print('Gracias por sumar')

'''try:
    #Codigo que queremos probar
    suma()
except TypeError:
#Codigo que se ejecuta si hay un error Exept
    print('Estas intentando concatenar tipos distintos')
except ValueError:
    print('Ese no es un numero')

else:
    #Codigo a ejecutar si no hay error
    print('Datos correctos')
finally:
    #codigo a ejecutar de todos modos
    print('Eso fue todo')'''

def pedir_numero():
    while True:
        try:
            numero=int(input('Ingrese un número: '))
        except:
            print('Ese no es un número')

        else:
            print(f'Ingresaste el número {numero}')
            break
    print('Gracias')
pedir_numero()