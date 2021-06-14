#Exercício Python #052 - Números primos
'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

tot = 0
numero = int(input("Digite um número: "))
for c in range(1 , numero + 1):
    if (numero % c) == 0:
        print('\033[33m', end= ' ')
        tot += 1
    else:
        print("\033[31m", end= ' ' )
    print(f'{c}', end= ' ')

print(f"\n\033[mO numero {numero} foi divisivel {tot} vezes")
if tot == 2:
    print("È por isso ele é primo")

else:
    print("E POR ISSO ELE NÂO È PRIMO")
