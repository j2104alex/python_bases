def perfumeria():
    for turno in range(1,1000):
        yield f'P-{turno}'

def farmacia():
    for turno in range(1, 1000):
        yield f'F-{turno}'

def cosmeticos():
    for turno in range(1, 1000):
        yield f'C-{turno}'

p=perfumeria()
f=farmacia()
c=cosmeticos()

def decorador(rubro):
    print('\n'+'*'*23)
    print('Su numero es: ')
    if rubro=='P':
        print(next(p))
    elif rubro=='F':
        print(next(f))
    else:
        print(next(c))
    print('Aguarde y será atendido')
    print('*'*23+'\n')

