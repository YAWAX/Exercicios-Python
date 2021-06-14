#Exercício Python #045 - GAME: Pedra Papel e Tesoura
#VITORIA -EMPATE- DERROTA
from random import randint
from time import sleep
itens = ('pedra' , 'papel' , 'tesoura')
computador = randint(0 , 2)
print("""Suas Opçoes:
[ 0 ] PEDRA 
[ 1 ] PAPEL]
[ 2 ] TESOURA""")
jogador = int(input("Qual é a sua jogada? "))
print('JO')
sleep(1)
print('Ken')
sleep(1)
print('PO!!!')

print('-=-' * 11)
print(f"Computador jogou {itens[computador]}" )
print(f"Jogador jogou {itens[jogador]}" )
print('-=-' * 11)
if computador == 0: #PEDRA
    if jogador == 0:
        print("EMPATE")

    elif jogador == 1:
        print("JOGADOR VENCE")

    elif jogador == 2:
        print("COMPUTADOR VENCE")

if computador == 1: #PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")

    elif jogador == 1:
        print("EMPATE")

    elif jogador == 2:
        print("JOGADOR VENCE")

if computador == 2: #TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")

    elif jogador == 1:
        print("COMPUTADOR VENCE")

    elif jogador == 2:
        print("EMPATE")

