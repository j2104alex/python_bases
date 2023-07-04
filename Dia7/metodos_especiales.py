#Tienen __nombre__ doble guion bajo al inicio y final
#Crear funcionalidades que no pueden ser representadas en un metodo regular

class CD:
    def __init__(self,autor,titulo,canciones):
        self.autor=autor
        self.titulo=titulo
        self.canciones=canciones

    def __len__(self):
        return self.canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __del__(self):
        print('Se ha eliminado el CD')

mi_cd=CD('Pink Floid','The wall',24)
print(mi_cd)
print(len(mi_cd))

#del mi_cd Eliminar mi cd