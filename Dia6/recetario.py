import os
from pathlib import Path
from os import system

ruta = Path(Path.home(),'Recetas')
categorias={'1':'carnes','2':'ensaladas','3':'pastas','4':'postres'}
menu= {'1':'Mostrar receta', '2':'Crear receta', '3':'Crear nueva categoria', '4':'Eliminar receta', '5':'Eliminar categoría', '6':'Finalizar menú'}
finalizar=False

def contar_recetas(ruta):
    contador=0
    for txt in Path(ruta).glob('**/*.txt'):
        contador+=1
    return contador
def bienvenida():
    nombre = input('Ingresa tu nombre :')
    print(f'Bienvenido al recetario {nombre}')

def ubicacion_recetas():
    os.chdir(ruta)
    ruta_recetas = ruta
    print(f'La ruta de las recetas se encuentra en: {ruta_recetas}')
    return ruta_recetas

def menu_eleccion():
    bienvenida()
    opcion_menu=''
    while opcion_menu not in menu.keys():
        print('OPCIONES MENÚ: ')
        for clave,opcion in menu.items():
            print(f'{clave}: {opcion}')
        opcion_menu=input('Ingrese un número del 1 al 6: ')
    return opcion_menu,menu[opcion_menu]

def opciones_elegidas(opcion_menu,categoria):
    ubicacion_carpeta_receta=ubicacion_recetas()
    match opcion_menu:
        case '1':
            leer_receta(categoria)
        case '2':
            crear_receta()
        case '3':
            crear_categoria()
        case '4':
            eliminar_receta()
        case '5':
            eliminar_categoria()
        case '6':
            finalizar_ejecucion()


def elegir_categoria():
    categoria_elegida=''
    while categoria_elegida not in categorias.keys():
        print('CATEGORIAS')
        for id,categoria in categorias.items():
            print(f'{id}: {categoria}')
        categoria_elegida=input('Ingrese una categoría del 1 al 4: ')
    return categoria_elegida,categorias[categoria_elegida]

def leer_receta():
    id_categoria, categoria = elegir_categoria()
    ruta_recetas=ubicacion_recetas()
    recetas_ruta=ruta_receta(ruta_recetas,categoria)
    id_receta_elegida,nombre_receta_elegida=(mostrar_recetas(recetas_ruta))
    abrir_archivo=open(os.path.join(ruta_recetas,categoria,nombre_receta_elegida))
    contenido=abrir_archivo.read()
    print(contenido)
    abrir_archivo.close()
    menu_eleccion()

def ruta_receta(ruta_recetas,categoria):
    ruta_categoria=os.path.join(ruta_recetas,categoria)
    recetas_categoria=os.listdir(ruta_categoria)
    return recetas_categoria

def mostrar_recetas(recetas_categoria):
    print(f'RECETAS DISPONIBLES')
    for i,receta in enumerate(recetas_categoria):
        print(f'{i+1} {receta}')
    receta_elegida=seleccionar_receta(recetas_categoria)
    return receta_elegida,recetas_categoria[receta_elegida-1]
def seleccionar_receta(recetas_categoria):
    receta_elegida = 0
    while receta_elegida not in range(1, len(recetas_categoria) + 1):
        receta_elegida = int(input('¿Qué receta desea elegir?: '))
    return receta_elegida

def crear_receta():
    id_categoria,categoria=elegir_categoria()
    print(categoria)

def crear_categoria():
    categoria = elegir_categoria()
    print(categoria)

def eliminar_categoria():
    categoria = elegir_categoria()
    print(categoria)
def eliminar_receta():
    categoria = elegir_categoria()
    print(categoria)

def finalizar_ejecucion():
    finalizar=True



id_menu,opcion_menu=(menu_eleccion())
print(id_menu,opcion_menu)
id_categoria,categoria=elegir_categoria()




