def chequear_3_cifras(lista):
    lista_3_cifras=[]
    for numero in lista:
        if numero in range(100,1000):
            lista_3_cifras.append(numero)
        else:
            pass
    return lista_3_cifras



resultado=chequear_3_cifras([555,99,600])
print(resultado)

lista_numeros=[100,5,56,100,0]
def todos_positivos(lista):
    for numero in lista_numeros:
        if numero<0:
            return False
    return True

print(todos_positivos(lista_numeros))

lista_numeros=[100,50,20,-100]

def suma_menores(lista_numeros):
    resultado = 0
    for numero in lista_numeros:
        if numero >=0:
            resultado+=numero
    return resultado

print(suma_menores(lista_numeros))

def cantidad_pares(lista_numeros):
    contador=0
    for numero in lista_numeros:
        if numero%2==0:
            contador+=1
    return contador

print(cantidad_pares([100,2,3,0]))