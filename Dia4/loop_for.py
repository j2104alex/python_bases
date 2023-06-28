#loop for
nombres=['Juan','Ana','Carlos','Belen']

for elemento in nombres:
    print(f'Hola {elemento}')

lista=['a','b','c']

for element in lista:
    element_number=lista.index(element)+1
    print(element,element_number)

names=['Pablo','Laura','Fede','Luis','Julia']

for name in names:
    if name.startswith('L'):
        print(name)
    else:
        print('No comienza con l')

numbers=[1,2,3,4,5]
value=0
for number in numbers:
    value=value+number
    print(value)

word='python'

for letter in word:
    print(letter)

for letter in 'python':
    print(letter)

for object in [[1,2],[3,4],[5,6]]:
    print(object)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
print('Diccionario')
dic={1:'a',2:'b',3:'c'}

for item in dic:
    print(item)
for item in dic.values():
    print(item)
for item in dic.items():
    print(item)