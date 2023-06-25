text='Hola'
text2='Esta es una prueba'

print(f"Index {text.index('o')}")
print(f"Index {text[3]}")
print(f"Index {text[0]}")
print(f"Index {text[-3]}")
print(f"Index {text[-4]}")

print(f"Index {text2.index('prueba')}")

print(f"Index {text2.index('a')}")
print(f"Index {text2.index('a',5)}")
#parametro, posicion inicial, posicion final
print(f"Index {text2.index('a',5,11)}")
#Buscar de derecha a izquierda
print(f"Index {text2.rindex('a')}")

