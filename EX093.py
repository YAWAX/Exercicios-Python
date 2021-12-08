Jogador = dict()          # 18 linhas de código
Jogador['Nome'] = str(input("Nome Do Jogador? "))
Partidas = int(input(f"Quanta Partidas {Jogador['Nome']} Jogou? "))
print()
Jogador['Gols'] = list()

for c in range(1, Partidas+1):
    Jogador['Gols'].append(int(input(f"Quantos Gols Na Partida {c}: ")))
Jogador['Total'] = sum(Jogador['Gols'])
print('-='*30)
print(Jogador)
print('-='*30)

for k, v in Jogador.items():
    print(f"O Campo {k} Tem Valor: {v}")
print('-='*30)
print(f"O Jogador {Jogador['Nome']} Jogou {Partidas} Partidas")

for f in range(1, Partidas+1):
    print(f"Na Partida {f}, {Jogador['Nome']} Fez {Jogador['Gols'][f-1]}")
print(f"Foi Um Total De {Jogador['Total']}")
