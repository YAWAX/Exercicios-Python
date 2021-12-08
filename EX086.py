matrix  = [[ ], [ ], [ ]]
matrix1 = [[ ], [ ], [ ]]
matrix2 = [[ ], [ ], [ ]]

for c in range(0, 3):
    Dado = int(input(f"Valor Para Matrix A{c}: "))
    matrix[c].append(Dado)

for c in range(0, 3):
    Dado = int(input(f"Valor Para Matrix B{c}: "))
    matrix1[c].append(Dado)

for c in range(0, 3):
    Dado = int(input(f"Valor Para Matrix C{c}: "))
    matrix2[c].append(Dado)

print("=="*20)
print(f'{matrix}\n{matrix1}\n{matrix2}')
