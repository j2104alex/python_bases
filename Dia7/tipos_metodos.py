#Decoradores permiten crear diferentes tipos de metodos

class Pajaro:
    alas=True

    def __init__(self,color,especie):
        self.color=color
        self.especie=especie

    def piar(self):
        print(f'pio, mi color es {self.color}')

    def volar(self,metros):
        print(f'Voló {metros} mts')
        self.piar()

    def pintar_negro(self):
        self.color='negro'
        print(f'Ahora el pajaro es de color {self.color}')

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'Puso {cantidad} de huevos')
        #No puedo acceder a self
        #Puedo acceder a atributos de clase
        cls.alas=False

    @staticmethod
    def mirar():
        print('El pajaro mira')

piolin=Pajaro('amarillo','canario')

print(piolin.volar(50))

print(piolin.alas)

#Metodo de clase
Pajaro.poner_huevos(30)

print(Pajaro.alas)
print(Pajaro.mirar())


