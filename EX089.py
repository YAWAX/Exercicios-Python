
ficha = list()

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    sair = str(input("Deseja Sair? ")).upper().title()
    if sair == 'S':
        break

print("-="*30)
print(f"{'N°':<4}{'Nome':<10}{'Média':>8}")

for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print("-"*35)
    opc = int(input("Mostrar Notas De Qual Aluno?: "))
    
    if opc == 999:
        break

    if opc <= len(ficha) - 1:
        print(f"Notas De {ficha[opc][0]} São {ficha[opc][1]}")

print("<<< VOLTE SEMPRE >>>")
