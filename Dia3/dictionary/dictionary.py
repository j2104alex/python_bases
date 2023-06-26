#Concepto y definicion/valor {} no tienen orden
#Mutable y admite valores duplicados en el valor, no en la clave
cliente={
    'nombre':'Juan',
    'apellido':'Perez',
    'peso':88,
    'talla':1.76
}

print(cliente)

result=cliente['apellido']
print(result)

dic={
    'c1':55,
    'c2':[10,20,30],
    'c3':{'s1':100,
          's2':200}
    }

print(dic['c3']['s2'])

dic2={
    'c1':['a','b','c'],
    'c2':['d','e','f'],
}

print(dic2['c2'][1].upper())

dic3={
    1:'a',
    2:'b'
}
dic3[3]='c'
dic3[1]='A'

print(dic3)

#Imprimir llaves
print(dic3.keys())
#Imprimir valores
print(dic3.values())
#Imprimir_todo el diccionario
print(dic3.items())