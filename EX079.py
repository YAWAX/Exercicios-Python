valores = []
sair = ''

while sair != 'N':
    n = int(input("Valor: "))

    while n in valores:
        print("Valor Duplicado")
        n = int(input("Valor: "))

    else:
        valores.append(n)

    sair = str(input("Deseja Continuar: ")).upper()

print(sorted(valores))
