import random
def lanzar_moneda():
    resultado=random.choice(['Cara', 'Cruz'])
    return resultado

lista_numeros=[1,5,7,8,9]

def probar_suerte(resultado_moneda,lista_numeros):
    if resultado_moneda=='Cara':
        print('La lista se autodestruirá')
        return []
    else:
        print('La lista fué salvada')
        return lista_numeros

resultado=lanzar_moneda()
print(probar_suerte(resultado,lista_numeros))