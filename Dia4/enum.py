lista=['a','b','c']
for indice, item in enumerate(lista):
    print(indice,item)
for indice, item in enumerate(range(1,10)):
    print(indice,item)

#fuera de loops
mis_tuples=list(enumerate(lista))

print(mis_tuples)

lista_indices=list("Python")

print(lista_indices)