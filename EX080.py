""" Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre
a lista ordenada na tela. """

n1 = []
while True:
    n = int(input("Valor: "))
    n1.append(n)

    if len(n1) == 5:
        break

print(n1)
