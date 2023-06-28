def mi_funcion(nombre):
       print(f'Hola {nombre}')

mi_funcion('Luis')

def multiplicar(num1,num2):
       total=num1*num2
       return total

print(multiplicar(1,2))

def invertir_palabra(palabra):
    palabra=palabra.upper()
    lista= list(palabra)
    reves =lista.reverse()
    return reves

print(invertir_palabra('palabra'))