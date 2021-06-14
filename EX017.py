from math import hypot
cateto_oposto = float(input("cateto oposto: "))
cateto_adjacente = float(input("cateto adjacente: "))
hi = hypot(cateto_oposto , cateto_adjacente)
print("A hipotenusa vai medir {:.2f}".format(hi))