"""
Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""

soma = cont = sair = 0

while sair != 999:
    n1 = int(input("Digite Um Valor: [999 Para Sair] "))
    if n1 == 999:
        sair += 999
    cont += 1
    soma += n1

print(f"Você Digitou {cont-1} números\nA Soma Deles é {soma-999}")
