precios_cafe=[
    ('capuchino',1.5),
    ('expresso',2.5),
    ('moka',1.9)
]

def cafe_mas_caro(lista_precios):
    precio_mas_caro=0
    cafe_mas_caro=''

    for cafe,precio in precios_cafe:
        if precio>precio_mas_caro:
            precio_mas_caro=precio
            cafe_mas_caro=cafe

    return((cafe_mas_caro,precio_mas_caro))

cafe,precio=cafe_mas_caro(precios_cafe)

print(f'El café mas caro es {cafe} cuyo precio es {precio}')