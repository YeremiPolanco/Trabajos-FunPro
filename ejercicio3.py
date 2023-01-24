print("PROGRAMA DE PRESUPUESTO DE HOSPITAL")
presupuesto = float(input("ingrese la cantidad de su presupuesto: "))

urgencias = presupuesto * 0.37 
pediatria = presupuesto * 0.42
traumatologia = presupuesto * 0.21

print("el presupiuesto de urgencias es: ", urgencias, "que representaria al 37%")
print("el presupiuesto de pediatria es: ", pediatria, "que representaria al 42%")
print("el presupiuesto de traumatologia es: ", traumatologia, "que representaria al 21%")