#Mientras que se cumpla una condicion
monedas = 5
while monedas > 0:
    print(f'Tengo {monedas}')
    monedas-=1
else:
    print('No tengo mas dinero')

respuesta='s'

while respuesta =='s':
    respuesta=input('Quieres seguir? (s/n)')
else:
    print('Gracias')

nombre=input('Tu nombre: ')

#Break-continue

