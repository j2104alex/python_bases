#Combiar dos o mas listas en tupples
nombres=['Ana','Hugo','Valeria']
edades=[65,29,42,58]
ciudades=['Lima','Madrid','Mexico']
combinados=list(zip(nombres,edades,ciudades))

print(combinados)

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} y vive en {ciudad}')