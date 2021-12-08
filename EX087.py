matrix  = [[ ], [ ], [ ]]
matrix1 = [[ ], [ ], [ ]]
matrix2 = [[ ], [ ], [ ]]
pares = []
somaterceiracoluna = 0

for c in range(0, 3):
    Dado = int(input(f"Valor Para Matrix A{c}: "))
    if Dado % 2 == 0:
        pares.append(Dado)
    if c == 2:
        somaterceiracoluna += Dado
    matrix[c].append(Dado)

for c in range(0, 3):
    Dado = int(input(f"Valor Para Matrix B{c}: "))
    if Dado % 2 == 0:
        pares.append(Dado)
    if c == 2:
        somaterceiracoluna += Dado
    matrix1[c].append(Dado)

for c in range(0, 3):
    Dado = int(input(f"Valor Para Matrix C{c}: "))
    if Dado % 2 == 0:
        pares.append(Dado)
    if c == 2:
        somaterceiracoluna += Dado
    matrix2[c].append(Dado)

print("=="*20)
print(f'{matrix}\n{matrix1}\n{matrix2}')
print("=="*20)
print(f"A Soma Dos Valores Pares é {sum(pares)}")
print(f"A Soma Dos Valores Da Terceira Coluna é {somaterceiracoluna}")
print(f"O Maior Valor Da Segunda Linha é {max(matrix1)}")
print("=="*20)
