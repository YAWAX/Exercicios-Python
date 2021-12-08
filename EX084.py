"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
Pessoas = list()
Dados = list()
maior = menor = 0

while True:
    print("———"*10)
    Dados.append(str(input("Nome: ")))
    Dados.append(float(input("Peso: ")))

    if len(Pessoas) == 0:
        maior = menor = Dados[1]

    else:
        if Dados[1] > maior:
            maior = Dados[1]

        if Dados[1] < menor:
            menor = Dados[1]

    Pessoas.append(Dados[:])
    Dados.clear()
    sair = str(input("Deseja Continuar? ")).upper()

    if sair == 'N':
        break

print()
print(f"\n{len(Pessoas)} Pessoas Cadastradas")
print(f"O Maior Peso Foi De {maior}Kg Peso De ", end="")

for p in Pessoas:
    if p[1] == maior:
        print(f"{p[0]}", end="")

print()
print(f"O Menor Peso foi de {menor}KG. Peso De ", end='')

for p in Pessoas:
    if p[1] == menor:
        print(f"{p[0]}", end='')
  
print()
