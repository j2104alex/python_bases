
from random import choice

lista=['gato','perro','camaleon','ahorcado','tiburon','dinosaurio']
guiones=[]
letras_correctas=[]
letras_incorrectas=[]
intentos=6
aciertos=0
juego_terminado=False

def elegir_palabra_azar(lista):
    palabra_elegida=choice(lista)
    letras_unicas=len(set(palabra_elegida))
    return palabra_elegida,letras_unicas

def pedir_letra():
    letra_elegida=''
    es_valida=False
    abcdario='abcdefghijklmnopqrstuwxyz'

    while not es_valida:
        letra_elegida = input('Ingrese una letra: ')
        if letra_elegida in abcdario and len(letra_elegida)==1:
            es_valida=True
        else:
            print('No has elegido una letra correcta')
    return letra_elegida
def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta=[]

    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))

def chequear_letra_usuario(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin=False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias+=1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Ya has encontrado esa letra, intentalo con una diferente')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas-=1

    if vidas==0:
        fin=perder()
    elif coincidencias==letras_unicas:
        fin=ganar(palabra_oculta)

    return vidas, fin, coincidencias
def perder():
    print('Te has quedado sin vidas')
    print(f'La palabra oculta era {palabra}')

    return True
def ganar(palabra_descubrierta):
    mostrar_nuevo_tablero(palabra_descubrierta)
    print('Felicitaciones, has encontrado la palabra!!!')

    return True

palabra,letras_unicas =elegir_palabra_azar(lista)
while not juego_terminado:
    print('\n'+'*'*20+'\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print(f'Letras incorrectas: '+'-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra= pedir_letra()

    intentos,terminado,aciertos=chequear_letra_usuario(letra,palabra,intentos,aciertos )

    juego_terminado=terminado