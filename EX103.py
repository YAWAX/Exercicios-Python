def Ficha(Nome='', Quantidade=''):
    """
    :param Nome: Nome Do Indivuduo
    :param Quantidade: Quantidade De Gols Do Jogador
    :return: {Nome} Fez {Quantidade} Gols No Campeonato
    """
    if Nome == '':
        Nome = '<Desconhecido>'
    if Quantidade == '':
        Quantidade = 0
    return f"{Nome.capitalize()} Fez {Quantidade} Gols No Campeonato"


Jogador = input("Nome: ")
gols = input('gols: ')
print(Ficha(Jogador, gols))
