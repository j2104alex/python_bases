class Padre:
    def hablar(self):
        print('Hola')
class Madre:
    def reir(self):
        print('ja,ja')

    def hablar(self):
        print('Que tal')
class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    pass

nieto=Nieto()
nieto.hablar() #Hereda de la primer clase,
nieto.reir()

#Orden en que se resuelve herencia de Nieto
print(Nieto.__mro__)