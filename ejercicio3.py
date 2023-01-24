print("PROGRAMA DE PRESUPUESTO DE HOSPITAL")
presupuesto = float(input("ingrese la cantidad de su presupuesto: "))

urgencias = presupuesto * 0.37 
pediatria = presupuesto * 0.42
traumatologia = presupuesto * 0.21

print("el presupuesto de urgencias es: ", urgencias, "que representaría al 37%")
print("el presupuesto de pediatría es: ", pediatria, "que representaría al 42%")
print("el presupuesto de traumatología es: ", traumatologia, "que representaría al 21%")
