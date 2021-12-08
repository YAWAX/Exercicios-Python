"""
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só 
será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele 
conquistou no final do jogo. 
"""
from pygame import mixer
import time
import random
vitorias = 0

while True:
    Número_Computador = random.randint(0 , 10)

    Número_Usuario = int(input("Diga Um Valor: "))
    Par_Ou_Impar = str(input("Par Ou Impar: ")).upper()

    Soma = Número_Computador + Número_Usuario


    if Soma % 2 == 0 and Par_Ou_Impar == "P": #Usuario Ganha
        print(f"Você jogou {Número_Usuario} o Computador Jogou {Número_Computador}. Total De {Soma} deu Par")
        print("VOCÊ VENCEU\n")
        vitorias += 1
    
    elif Soma % 2 != 0 and Par_Ou_Impar == "I": #Usuario Ganha     #Deu Impar    #Jogador Jogou Impar

        print(f"\nVocê jogou {Número_Usuario} o Computador Jogou {Número_Computador}. Total De {Soma} deu Impar")
        print("VOCÊ VENCEU\n")
    
    elif Soma % 2 == 0 and Par_Ou_Impar == 'I':#Usuario Perde      #Deu Par       #Jogador jogou Impar

        mixer.init()
        mixer.music.load('C:/Users/Renê/Documents/PYTHON-20210610T174151Z-001/PYTHON/musica.mp3')
        mixer.music.play()
        time.sleep(1)
        print(f"\nVocê jogou {Número_Usuario} o Computador Jogou {Número_Computador}. Total De {Soma} deu Par")
        print("VOCÊ Perdeu\n")
        break

    elif Soma % 2 != 0 and Par_Ou_Impar == "P":#Usuario Perde      #Deu Impar      #Jogador Jogou Par
    
        mixer.init()
        mixer.music.load('C:/Users/Renê/Documents/PYTHON-20210610T174151Z-001/PYTHON/musica.mp3')
        mixer.music.play()
        time.sleep(1)
        print(f"\nVocê jogou {Número_Usuario} o Computador Jogou {Número_Computador}. Total De {Soma} deu Par")
        print("VOCÊ PERDEU\n")
        break

if vitorias == 0:
    print("\nAcho Bom Você Ir Se Convesar. Não Ganhou Nenhuma Vez ksksksk ruim demais\n")

elif vitorias == 1:
    print("\nVocê Ganhou Uma Vez Apenas\n")

elif vitorias == 2:
    print("\nVocê Ganhou Duas Vezes. Sua Sorte Ta ruim ein mano ksksks\n")

elif vitorias == 3:
    print(f"\ncarai ta brabo ein mano slk. Acertou {vitorias}\n")

else:
    print(f"\nCaralho Mano Tu é Bom ein acertou {vitorias}\n")

#from pygame import mixer
#mixer.init()
#mixer.music.load('C:/Users/Renê/Documents/PYTHON-20210610T174151Z-001/PYTHON/musica.mp3')
#mixer.music.play()
