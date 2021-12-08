from random import randint

def sorteia(lista):         #Função Para Sortea Valores
    for c in range(0, 5):
        lista.append(randint(1, 10))


def SomaPar(lista):        #Função Para Somar Pares
    soma= 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando OS Valores Pares de {lista}, temos {soma}")


numeros = list()
sorteia(numeros)
SomaPar(numeros)
