"""Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while."""

print('=' * 25)
print("10 TERMOS DE UMA PA")
print('=' * 25 )

a1 = int(input("PRIMEIRO TERMO: "))  #termo
r = int(input("Razão: "))  #razâo
termo = a1
cont = 1

while cont <= 10:
    print(termo)
    termo += r
    cont += 1
