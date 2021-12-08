from random import randint
from time import sleep

palpites = int(input("Quantos Jogos: "))
jogos = list()
lista = list()
cont1 = 1
print(f"\n===—Gerando {palpites} Jogos—===")

while cont1 <= palpites:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    cont1 += 1
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
