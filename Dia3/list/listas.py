#Son mutables y pueden tener varios tipos de datos
#ordenados y admite duplicados
mi_lista=['a','b','c']
mi_lista2=['d','e','f']
mi_lista3=mi_lista+mi_lista2

mi_lista3[0]='alfa'
#Agregar al final
mi_lista3.append('g')
#Eliminar elementos el último si no se pone nada
eliminar= mi_lista3.pop()
#Eliminar elementos segun index
mi_lista3.pop(0)

print(type(mi_lista))
print(len(mi_lista))
print(mi_lista[0])

print(mi_lista+mi_lista2)
print(mi_lista3, eliminar)


orden_lista=['g','o','b','m','c']
#ordenar alfabeticamente y no devuelve nada, no se puede asignar
orden_lista.sort()
#Devuelve del fin al inicio
orden_lista.reverse()

print(orden_lista)