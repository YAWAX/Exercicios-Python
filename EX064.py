"""Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O
programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No 
final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

n1 = int(input("Digite Números Inteiros: "))
soma = n1
cont = 0

while n1 != 999:
    n1 = int(input("Digite Números Inteiros: "))
    if n1 == 999:
        soma -= 999
    soma += n1
    cont += 1

print(f"Foram Digitados {cont} números\nA Soma entre eles é {soma} ")
