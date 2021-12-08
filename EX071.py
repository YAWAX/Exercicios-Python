"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai 
informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

valor_sacado = int(input("\nQuanto Deseja Sacar: "))
nota50 = nota20 = nota10 = nota1 = 0

while True:
    if valor_sacado >= 50:
        nota50 += 1
        valor_sacado -= 50
    
    elif valor_sacado >= 20:
        nota20
        valor_sacado -= 20
    
    elif valor_sacado > 10:
        nota10 += 1
        valor_sacado -= 10

    elif valor_sacado >= 1:
        nota1
        valor_sacado -= 1

    else:
        break

print(f"Cedulas De Cinquenta: {nota50}")
print(f"Cedulas De Vinte: {nota20}")
print(f'Cedulas De Dez: {nota10}')
print(f"Cedulas De Um: {nota1}")
