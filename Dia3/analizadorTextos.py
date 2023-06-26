#Ingresar un texto, ingrese 3 letras

#1. Cuantas veces aparece cada letra (convertir a min letras y texto)
#2. Cuantas palabras hay?(Lista y largo)
#3. Primer letra y ultima
#4. invertir el orden de la lista y luego orden
#5. Si python aparece dentro del texto bool, diccionario

#Lista que contiene las letras
letters=[]
#Variable para almacenar el texto
text=input('Ingrese un texto: ').lower()

#Ciclo para ingresar letras
for _ in range(3):
    letters.append(input('Ingrese una letra: ').lower())

#Variable para almacenar la lista de text por palabras
textListWords=text.split()

#Convertir texto en una lista por letras
text_List=list(text)


firstCounter=text.count(letters[0])
secondCounter=text.count(letters[1])
thirdCounter=text.count(letters[2])
python=False

print(f'Cantidad de veces {letters[0]}: {firstCounter}, {letters[1]}: {secondCounter}, {letters[2]}: {thirdCounter}')
print(f'Hay {len(textListWords)} palabras')
print(f'La primer letra es {text_List[0]} y la última letra es {text_List[-1]}')

textListWords.reverse()
reves_unido=' '.join(textListWords)

print(f'El texto invertido es: {reves_unido}')

buscar_python= 'python' in text
dic= {True:'si', False:'no'}
print(f'La palabra Python {dic[buscar_python]} se encuentra en el texto')
