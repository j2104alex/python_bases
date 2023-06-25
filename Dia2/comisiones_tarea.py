nombre=input("Ingresa tu nombre:")
ventas=int(input("Ingresa el valor de ventas:"))

print(f"Estimado {nombre} el valor de las comisiones por el monto total de ventas es: $ {round(ventas*0.13,2)}")