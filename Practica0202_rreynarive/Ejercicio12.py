inicio = 3.49
pan_nofresco = (inicio - (inicio * 0.6))
final = round(pan_nofresco, 2)

compra = int(input("¿Cuantas barras va a comprar?"))

print("Precio habitual de una barra de pan es", inicio, "€")
print("Por no ser fresco el precio es", final, "€")

operacion = compra * final
pa_final = round(operacion, 2)

print("El coste de su compra es", pa_final, "€")