peso = float(input("Introduzca su peso (kg):"))
altura = float(input("introduzca su altura (m):"))
imc = peso / (altura**2)
indice = round(imc, 2)
print("Tu indice de masa corporal es de", indice)
