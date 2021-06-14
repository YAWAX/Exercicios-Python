"""Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

n1 = int(input('Digite Um Valor Para Fatorial: '))
c = n1
f = 1
while c > 0:
    f *= c
    c -= 1
print(f)
