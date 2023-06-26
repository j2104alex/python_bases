
text="ABCDEFGHIJKLMNOPQRSTUWXYZ"
fragment=text[2]
#Desde el index 2 al 5 sin incluir
fragment2=text[2:5]
#Desde el 2 hasta donde se pueda
fragment3=text[2:]
#Desde el inicio hasta el 5 sin incluir
fragment3=text[:5]
#Desde el index 2 al 10 sin incluir salteando 2 caracteres
fragment4=text[2:10:2]
#Desde imprime todos al reves
fragment5=text[::-1]
print(fragment)
print(fragment2)
print(fragment3)
print(fragment4)
print(fragment5)