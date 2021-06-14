#Exercício Python #049 - Tabuada v.2.0
'''
Exercício Python 049: Refaça o DESAFIO 009,
mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for.

'''

r = int(input('DIGITE UM NUMERO PARA VER A TABUADA: '))
for c in range(1 , 11):
    print(f" {c} x {r} = {c * r} ")
