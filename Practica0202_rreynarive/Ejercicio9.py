euros = float(input("Cantidad a invertir:"))
interes = float(input("Interes anual(%):"))
años = int(input("Cuantos años:"))

capital = euros + ((euros*interes*años)/100)
print("La capital de la inversion es de", capital, "€")
