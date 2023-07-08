def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
    return otra_funcion

def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())

mayuscula_decorada=decorar_saludo(mayusculas)
mayuscula_decorada('Fede')