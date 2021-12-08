from random import randint
from operator import itemgetter

Game = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)}

ranking = list()

for k, v in Game.items():
    print(f"{k} tirou {v} No Dado")

print()
ranking = sorted(Game.items(), key=itemgetter(1), reverse=True)
print("  === RANKING DOS JOGADORES ===")

for i, v in enumerate(ranking):
    print(f"    {i+1}° lugar: {v[0]} Com {v[1]}")
