print("PROGRAMA QUE DETERMINA LAS MULTIPLES AREAS DE UN CILINDRO")
r = float(input("ingrese la medida de su radio: "))
h = float(input("ingrese la medida de su altura: "))

area_base = 3.1416 * (r ** 2)
area_lateral = 2 * 3.1416 * r * h
area_total = 2 * area_base + area_lateral

print("su área de la base es: ", area_base)
print("su área lateral es: ", area_lateral)
print("su área total es: ", area_total)