"""
Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

valor = 0
while True:
    numero = int(input("Valor Para tabuada: "))
    if numero <= 0:
        break

    valor = 0
    for c in range(1, 11):
        valor += 1
        print(f"{numero} x {valor} = {numero * valor}")    

print("Tabuada Finalizada. :)")
