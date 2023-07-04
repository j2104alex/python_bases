class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance=0):
        super().__init__(nombre,apellido)
        self.numero_cuenta=numero_cuenta
        self.balance=balance

    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellido}.\nBalance de cuenta {self.numero_cuenta}: ${self.balance}'

    def depositar(self,monto_deposito):
        self.balance+=monto_deposito
        print('Deposito aceptado')

    def retirar(self,monto_retirar):
        if self.balance>=monto_retirar:
            self.balance-=monto_retirar
            print('Retiro aceptado')
        else:
            print('Fondos insuficientes')


def crear_cliente():
    nombre_cl=input('Ingresa tu nombre: ')
    apellido_cl=input('Ingresa tu apellido: ')
    numero_cuenta_cl=input('Ingresa tu numero de cuenta: ')
    saldo_cl=int(input('Ingresa tu saldo: '))
    cliente=Cliente(nombre_cl,apellido_cl,numero_cuenta_cl,saldo_cl)
    return cliente
def inicio():
    mi_cliente=crear_cliente()
    print(mi_cliente)
    opcion=0
    while opcion != 'S':
        print('Elije: Depositar(D), Retirar(R) o salir (S)')
        opcion=input()

        if opcion=='D':
            monto_deposito=int(input('Monto a depositar'))
            mi_cliente.depositar(monto_deposito)
        elif opcion=='R':
            monto_retiro=int(input('Monto a retirar: '))
            mi_cliente.retirar(monto_retiro)
        print(mi_cliente)
    print('Gracias por operar en Banco Python')
inicio()