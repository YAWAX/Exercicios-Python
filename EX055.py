"""Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre 
qual foi o maior e o menor peso lidos. """

peso = []
for c in range(1, 6):
    Peso1 = float(input(f"Peso Da {c}° Pessoa: "))
    peso.append(Peso1)

print(f"\nO Maior Peso foi {max(peso)}\nO Menor Peso Foi {min(peso)}\n")
