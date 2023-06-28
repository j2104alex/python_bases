# **kwargs

def suma(**kwargs):
    total=0
    #items() para acceder a clave y valor
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total+=valor
    return total

print(suma(x=3, y=5,z=2))

#Orden: def suma(num1,num2, *args, **kwargs):

def prueba(num1,num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg= {arg}')

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

#prueba(15,50,100,200,300,400,'x'='uno','y'='dos','z'='tres')
args=[100,200,300,400]
kwargs={'x':'uno','y':'dos','z':'tres'}
prueba(15,50,*args,**kwargs)

def describir_persona(**kwargs):
    print(f'Características de {nombre}:')
    for clave,valor in kwargs.items():
        print(f'{nombre_argumento}: {valor_argumento}')