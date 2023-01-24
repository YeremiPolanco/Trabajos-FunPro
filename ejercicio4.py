print("PROGRAMA QUE AYUDA A SABER EL SUELDO DE UN EMPLEADO MÁS SUS COMISIONES")
sueldo_base = float(input("ingrese su sueldo base: "))
venta_1 = float(input("ingrese el monto de su primera venta "))
venta_2 = float(input("ingrese el monto de su segunda venta "))
venta_3 = float(input("ingrese el monto de su tercera venta "))

v1_porcentaje = venta_1 * 0.10
v2_porcentaje = venta_2 * 0.10
v3_porcentaje = venta_3 * 0.10

sueldo_total = sueldo_base + v1_porcentaje + v2_porcentaje + v3_porcentaje
comision = v1_porcentaje + v2_porcentaje + v3_porcentaje

print("-------------------------------------------------------------------")
print("BOLETA DE SUELDO LISTA :)")
print("su sueldo base es: ", sueldo_base)
print("el porcentaje total ganado es de: ", comision)
print("considerando lo anterior su sueldo es de: ", sueldo_total)
