from random import  shuffle

#Lista inicial
palitos=['-','--','---','----']

#Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

mezclar(palitos)
print(palitos)

#Probar suerte
def probar_suerte():
   numero=''

   while numero not in ['1','2','3','4']:
       numero=input('Ingresa un número del 1 al 4: ')

   return int(numero)

#Comprobar intento

def chequear_intento(lista,intento):
    if (lista[intento-1])=='-':
        print('A lavar los platos!')
    else:
        print('Esta vez te salvaste')

    print(f'Te ha tocado {lista[intento-1]}')

palitos_mezclados=mezclar(palitos)
seleccion=probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

lista_numeros = [1, 2, 15, 7, 2, 8]


def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista


def promedio(lista):
    valor_medio = sum(lista) / len(lista)
    return valor_medio