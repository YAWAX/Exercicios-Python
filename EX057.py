"""Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = str(input("Qual Seu Sexo: [M/F] ")).upper().strip()[0]

while sexo != "M" and sexo != "F":
    print("Valor Invalido Digite Novamente")
    sexo = str(input("Qual Seu Sexo: [M/F] ")).upper().strip()

print(f"Obrigado, Seu Gênero Foi Registrado Com Sucesso")
