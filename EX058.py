"""Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um 
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer."""

import random
vermelho = "\033[1;31m"
verde = "\033[1;32m"
amarelo = "\033[1;33m"
ciano = "\033[1;36m"
fimcor = "\033[0;0m"

print(f"\n{amarelo}===Vamos Jogar, Eu Vou Pensar Em Um Número e Você Tenta Advinhar==={fimcor}\n")
Tentativas = 0
N1 = int(input("Digite Um Número: "))
N2 = random.randint(0, 10)
print(N2)

while N1 != N2:
    if N1 != N2:
        print(f"{ciano}Você Errou, Tente Novamente{fimcor}")
        Tentativas += 1
        DICA = str(input("Você Quer Uma Dica? ")).upper()
        if DICA == "S":
            if N1 > N2:
                print("Digite Um Valor Menor")
            if N1 < N2:
                print("Digite Um Valor Maior")
    
    N1 = int(input("\nDigite Um Número: "))

if Tentativas == 0:
    print(f"\n{verde}Você Ta Com A Sorte Afiada. Acertou De Primeira{fimcor}\n")

elif Tentativas == 1:
    print(f"\n{verde}Você Ta Com A Sorte Afiada. Acertou Quase De Primeira{fimcor}\n")

elif Tentativas >= 2 and Tentativas < 8:
    print(f"\n{vermelho}Você Deve Estar Em Um Dia ruim. Foram Necessarias {Tentativas}\n{fimcor}")

elif Tentativas > 8:
    print(f"\n{vermelho}Você Devia Ir Se Confessar. Foram Necessarias {Tentativas}\n{fimcor}")
