#() Dentro parentesis y son inmutables
#ordenados y admite duplicados
mi_tuple=(1,2,(10,20),4)

print(type(mi_tuple))
print(mi_tuple[2][0])

mi_tuple=list(mi_tuple)

print(type(mi_tuple))

t=(1,2,3,1)
#Debe haber la misma cantidad de elementos (desempacar)
x,y,z,a=t
print(x,y,z,a)
print(len(t))
#contar cuantas veces aparece
print(t.count(1))
#index
print(t.index(2))
