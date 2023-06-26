text="Este es el texto de Alexa"

result=text.upper()
result2=text.lower()
result3=text.split()

text1="Aprender"
text2="Python"
text3="es"
text4="genial"
result4=" ".join([text1,text2,text3,text4])

print(result)
print(result2)
print(result3)
print(result4)
print(text.find('texto'))
print(text.replace('texto','poema'))


texto='Si la implementación es difícil de explicar, puede que sea una mala idea.'

print(texto.replace('difícil','fácil').replace('mala','buena'))
