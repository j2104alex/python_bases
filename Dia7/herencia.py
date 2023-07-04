class Animal:

    def __init__(self,edad,color):
        self.edad=edad
        self.color=color
    def nacer(self):
        print('Este animal ha nacido')

class Pajaro(Animal):
    pass

#De quien heredo la clase
print(Pajaro.__bases__)

#Si quiero mirar a quien heredo
print(Animal.__subclasses__())

piolin=Pajaro(2,'amarillo')
piolin.nacer()

print(piolin.color)