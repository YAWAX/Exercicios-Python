#Exercício Python #042 - Analisando Triângulos v2.0

'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

r1 = float(input("Digite o comprimento de uma reta : "))
r2 = float(input("Digite o comprimento de uma reta : "))
r3 = float(input("Digite o comprimento de uma reta : "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("È POSSIVEL FORMAR UM TRIANGULO: ")

else:
    print("Não È Possivel formar um triangulo: ")

if r1 == r2 and r3 == r2 and r3 == r1:
    print("EQUILATERO")

if r1 == r2 and r3 != r1 and r3 != r2    or   r3 == r1 and r2 != r3   or r3 == r2 != r1:
    print('ISÓSCELES')

if r1 != r2 and r3 != r1 and r3 != r2:
    print("ESCALENO")
