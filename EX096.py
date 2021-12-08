def terreno(a, b):
    area = a * b
    print(f"A Area De Um Terrno {a}x{b} é de {area}²")


terreno(a=float(input("LARGURA (m): ")),
        b=float(input("Comprimento (m): ")))
