#Cuenta de ahorro
intereses_anuales = 4/100
deposito = float(input("Deposite su dinero:\n"))
calculo = deposito + (deposito*intereses_anuales)
final = round(calculo, 2)
calculo2 = deposito + (deposito*intereses_anuales*2)
final2 = round(calculo2, 2)
calculo3 = deposito + (deposito*intereses_anuales*3)
final3 = round(calculo3, 2)
print("Su ahorro en el primer año es", final)
print("Su ahorro en el segundo año es", final2)
print("Su ahorro en el tercer año es", final3)