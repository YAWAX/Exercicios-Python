"""Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. """

Termos = int(input("Quantos Termos Você Quer Mostrar: "))
cont = 3
n1 = 0
n2 = 1
print(f"{n1} x {n2}", end=" x ")

while cont <= Termos:
    cont += 1
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" x ")
