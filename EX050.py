#Exercício Python #050 - Soma dos pares
'''Exercício Python 050: Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

soma = 0
contador = 0

for c in range(0 , 6 ):
    numero_inteiro = int(input("DIGITE UM NUMERO INTEIRO: "))
    if numero_inteiro % 2 == 0:
        contador += 1
        soma += numero_inteiro

print(f"VOCÊ INFORMOU {contador} NUMEROS PARES.A SOMA DE TODOS OS VALORES SOLICITADOS É {soma}")
