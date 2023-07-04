#Los objetos pueden tomar diferentes formas
'''Dos objetos de clases distintas pueden ejecutar
un metodo con el mismo nombre y ejecutar cosas distintas'''
class Vaca:
    def __init__(self,nombre):
        self.nombre=nombre

    def hablar(self):
        print(self.nombre+' dice muuuu')

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')

vaca1=Vaca('Aurora')
oveja1=Oveja('Nube')

animales=[vaca1,oveja1]

for animal in animales:
    animal.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)