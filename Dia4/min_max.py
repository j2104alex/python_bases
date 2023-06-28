lista=[58,76,64,35]
menor=min(lista)
mayor=max(lista)
print(f'El menor es {menor} y el mayor es {mayor}')

nombres=['Juan','Pablo','Alicia','Carlos']
print(min(nombres))
#Busca primero en las mayusculas y luego minusculas
print(min('Carlos'))

dic={'c1':45,'c2':11}
print(min(dic))
print(min(dic.values()))