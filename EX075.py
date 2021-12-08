nove = 0
par = 0

n1 = int(input("VALOR 1: "))
n2 = int(input("VALOR 2: "))
n3 = int(input("VALOR 3: "))
n4 = int(input("VALOR 4: "))

tupla = (n1, n2, n3, n4)

for c in tupla:
    if c == 9:
        nove += 1
    
    if c % 2 == 0:
        par += 1

print(f"\nNùmeros Digitados: {tupla}\nNúmero Nove Apareceu: {nove}\nQuantidade De Pares: {par}\nO Valor Três Apareceu Na Posição {tupla.index(3)+1}\n")
