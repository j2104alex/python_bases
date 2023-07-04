class Pajaro:
    alas=True
    #Constructor con atributos
    def __init__(self,color,especie):
        self.color=color
        self.especie=especie

    #Metodos/Funciones
    #Siempre debe ir minimamente con un argumento obligatorio SELF
    #Hace referencia a cada instancia de cada objeto de la clase
    def piar(self):
        print(f'pio, mi color es {self.color}')

    def volar(self,metros):
        print(f'Voló {metros} mts')

piolin=Pajaro('amarillo','canario')

piolin.piar()
piolin.volar(50)