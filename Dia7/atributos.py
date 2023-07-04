

#Crear la clase
class Pajaro:
    #Atributos de clase
    alas=True

    # Atributos de instancia
    #Metodo constructor, entre parentesis se manda parametros, los atributos
    def __init__(self,color,especie):
        #Self hace referencia a cada instancia de la clase
        self.color=color
        #el color entre parentesis es el parametro
        #self.color es el atributo
        self.especie=especie

mi_pajaro=Pajaro('Rojo','Picaflor')


#Atributos de instancia
print(mi_pajaro.color,mi_pajaro.especie)
#Atributos de clase
print(Pajaro.alas,mi_pajaro.alas)