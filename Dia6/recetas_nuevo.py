import os
import shutil
from pathlib import Path
from os import system

ruta_recetas = Path(Path.home(),'Desktop','Recetas')
categorias={}
for i, subcarpeta in enumerate(os.listdir(ruta_recetas), start=1):
    if os.path.isdir(os.path.join(ruta_recetas, subcarpeta)):
        categorias[str(i)] = subcarpeta
menu= {'1':'Mostrar receta', '2':'Crear receta', '3':'Crear nueva categoria', '4':'Eliminar receta', '5':'Eliminar categoría', '6':'Finalizar menú'}
estado_finalizado=False

def contar_recetas(ruta):
    contador=0
    for txt in Path(ruta).glob('**/*.txt'):
        contador+=1
    return contador

def inicio():
    print('*'*50)
    print('*'*5+' Bienvenido al administrador de recetas '+'*'*5)
    print('*'*50)
    print(f'La ruta se encuentra en: {ruta_recetas}')
    print(f'Total recetas: {contar_recetas(ruta_recetas)}')
    menu_eleccion()

def menu_eleccion():
    opcion_menu=''
    while opcion_menu not in menu.keys() and estado_finalizado==False:
        print('OPCIONES MENÚ: ')
        print('*' * 50)
        for clave,opcion in menu.items():
            print(f'{clave}: {opcion}')
        opcion_menu=input('Ingrese un número del 1 al 6: ')
        system('cls')
    opciones_elegidas(opcion_menu)

def opciones_elegidas(opcion_menu):
    match opcion_menu:
        case '1':
            system('cls')
            #Elegir categoria
            categoria_id,nombre_categoria=elegir_categoria()
            #Elegir receta
            receta_id,nombre_receta=seleccionar_receta(nombre_categoria)
            #Leer receta
            leer_receta(nombre_categoria,nombre_receta)
            #Retornar menu
            retornar_menu()
        case '2':
            system('cls')
            nombre_receta=''
            contenido_receta=''
            # Elegir categoria
            categoria_id, nombre_categoria = elegir_categoria()
            system('cls')
            while len(nombre_receta)==0:
                nombre_receta=input('Dime el nombre de la receta que quieres crear: ')
            while len(contenido_receta)==0:
                contenido_receta=input('Dime el contenido de la receta que quieres crear: ')
            crear_receta(nombre_categoria,nombre_receta,contenido_receta)
            # Retornar menu
            retornar_menu()
        case '3':
            system('cls')
            nombre_categoria_nueva=''
            while len(nombre_categoria_nueva) == 0:
                nombre_categoria_nueva = input('Dime el nombre de la categoria que quieres crear: ')
            crear_categoria_nueva(nombre_categoria_nueva)
            # Retornar menu
            retornar_menu()
        case '4':
            system('cls')
            # Elegir categoria
            categoria_id, nombre_categoria = elegir_categoria()
            # Elegir receta
            receta_id, nombre_receta = seleccionar_receta(nombre_categoria)
            borrar_receta(nombre_categoria,nombre_receta)
            # Retornar menu
            retornar_menu()
        case '5':
            id_categoria, nombre_categoria=elegir_categoria()
            borrar_categoria(nombre_categoria)
            # Retornar menu
            retornar_menu()
        case '6':
            estado_finalizado=True
            print('Gracias por usar el recetario')

def elegir_categoria():
    system('cls')
    categoria_elegida=''
    while categoria_elegida not in categorias.keys():
        print('CATEGORIAS')
        print('*'*20)
        for id,categoria in categorias.items():
            print(f'{id}: {categoria}')
        categoria_elegida=input('Ingrese una categoría del 1 al 4: ')
        system('cls')
    return categoria_elegida,categorias[categoria_elegida]


def seleccionar_receta(categoria):
    system('cls')
    ruta_categoria=os.listdir(os.path.join(ruta_recetas,categoria))
    receta_elegida = 0

    while True:
        try:
            print(f'RECETAS DISPONIBLES {categoria.upper()}')
            print('*' * 20)
            for i, receta in enumerate(ruta_categoria):
                print(f'{i + 1} {receta}')
            receta_elegida = int(input('¿Qué receta desea elegir?: '))
            if receta_elegida in range(1, len(ruta_categoria) + 1):
                break
            else:
                system('cls')
                print('Opción inválida, por favor ingrese un número válido')
        except ValueError:
            system('cls')
            print('Opción inválida, por favor ingrese un número válido')
    system('cls')
    return receta_elegida, ruta_categoria[receta_elegida-1]

def leer_receta(categoria,receta):
    system('cls')
    abrir_archivo=open(os.path.join(ruta_recetas,categoria,receta))
    contenido=abrir_archivo.read()
    print(f'{receta.upper()}: \n{contenido}')
    abrir_archivo.close()

def crear_receta(categoria,nombre_receta,contenido_receta):
    system('cls')
    if not nombre_receta.endswith('.txt'):
        nombre_receta+='.txt'
    ruta_receta_nueva = open(os.path.join(ruta_recetas, categoria,nombre_receta),'a')
    ruta_receta_nueva.write(contenido_receta)
    ruta_receta_nueva.close()
    print(f'La receta {nombre_receta} creada con exito!')

def crear_categoria_nueva(nombre_categoria):
    ruta_categoria_nueva=os.path.join(ruta_recetas,nombre_categoria)
    os.mkdir(ruta_categoria_nueva)
    print(f'La categoría {nombre_categoria} fué creada con exito!')

def borrar_receta(nombre_categoria,nombre_receta):
    ruta_categoria_nueva = os.path.join(ruta_recetas, nombre_categoria,nombre_receta)
    os.remove(ruta_categoria_nueva)
    print(f'La receta {nombre_receta} fué eliminada con exito!')

def borrar_categoria(nombre_categoria):
    ruta_categoria_nueva = os.path.join(ruta_recetas, nombre_categoria)
    shutil.rmtree(ruta_categoria_nueva)
    print(f'La categoria {nombre_categoria} fué eliminada exitosamente')

def retornar_menu():
    estado=input('Ingresa cualquier letra/numero para continuar: ')
    system('cls')
    menu_eleccion()

inicio()
