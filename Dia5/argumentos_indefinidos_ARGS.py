# *arg no aceptan un numero determinado de argumentos en una funcion


def suma(*args):
    total=0
    for arg in args:
        total+=arg
    return total
print(suma(1,2,3))


def suma_cuadrados(*args):
    cuadrados = 0
    for arg in args:
        cuadrados += arg ** 2
    return cuadrados

print(suma_cuadrados(1,2,3))