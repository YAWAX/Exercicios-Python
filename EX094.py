""" Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média """

Pessoas = dict(list())
Tudo = list()
cont = 0
Idade = list()
MUlheresCAdastradas = list()
PessoasAcimaDAMEdia = list()

while True:
    Pessoas['nome'] = str(input("Nome: ")).upper()
    Pessoas['idade'] = int(input('idade: '))
    Idade.append(Pessoas['idade'])
    Pessoas['Sexo'] = str(input("Sexo: ")).upper()

    if Pessoas['Sexo'] == 'F':
        MUlheresCAdastradas.append(Pessoas['nome'])
    Tudo.append([Pessoas.copy()])
    cont += 1

    sair = str(input("Deseja Sair? ")).upper()
    if sair == 'S':
        break
    print()

TotalIDADE = 0
for c in Idade:
    TotalIDADE += c
media = TotalIDADE / cont

for a in Tudo:
    for i in a:
        if i['idade'] > media:
            PessoasAcimaDAMEdia.append(i['nome'])

print('-='*35)
print(f"Ao Todo Temos {cont} Pessoas Cadastradas")
print(f"A Media de idade Do Grupo é {media:.1f}")
print(f"Mulheres Cadastradas são: {MUlheresCAdastradas}")
print(f"Pessoas Acima Da Média: {PessoasAcimaDAMEdia}")
