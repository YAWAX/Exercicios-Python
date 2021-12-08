time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input("Nome Do Jogador: "))
    tot = int(input(f"Quantas Partidas {jogador['Nome']} Jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"Quantos Gols Na Partida {c+1}: ")))
    jogador['gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer Continuar? [S/N] ")).upper()
        if resp in 'SN':
            break
        print('Erro! Responda Apenas S Ou N')
    if resp == 'N':
        break
print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print('—'*40)

while True:
    busca = int(input("Mostrar Dados de Qual Jogador? (999 Para Parar)"))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não Existe Jogador Com Código {busca}')
    else:
        print(f" -- LEvantamento Do Jogador {time[busca]['Nome']}")
        for i, g in enumerate(time[busca]['gols']):
            print(f"    No Jogo {i+1} fez {g} gols")
    print("-"*40)

print("<< Volte Sempre >>")
