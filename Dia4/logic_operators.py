#Operadores comparación
#Se obtiene un bool
#Asignación = y comparación ==

mi_variable='Rojo'
mi_bool= 10==25 #False
mi_bool= '100' == 100 #False
mi_bool=100.0 ==100 #True
bool=100!=99 #True

print(mi_bool, bool)

booleano= 4<5 or 3 == 30

print(booleano)
#operadores logicos and or not

text='Esta frase es breve'

bool2= ('frase' in text) and ('python' in text)
bool3= ('frase' in text) or ('python' in text)
bool4= not ('a' =='a')
print(bool2,bool3,bool4)

