#Set solo admite un elemento
#No se repite, si se repite los descarta
#No estan ordenados, no tiene index
#Son inmutables, no se puede añadir listas ni diccionarios

#Por eso en este caso de debe poner un conjunto de llaves
set ([1,2,3,4,5,6])
#Se pueden poner directamente
{1,2,3,4,5,6}

mi_set=set([1,2,3,4,5])
otro_set={1,2,3}
print(len(mi_set))
print(2 in mi_set)

s1= {1,2,3}
s2= {3,4,5}
#Añadir
s1.add(6)
#Eliminar
s1.remove(6)
#Descartar
s1.discard(7)
#Eliminar un elemento aleatorio
sorteo= s1.pop()
s3=s1.union(s2)
#Limpiar el set
#s3.clear()

print(sorteo)
print(s3)