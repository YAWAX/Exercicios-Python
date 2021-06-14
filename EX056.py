"""Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No 
final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e 
quantas mulheres têm menos de 20 anos."""

idade1 = []
mulheres_Menos_De_Vinte = 0
Nome_homem_Mais_Velhos = ''
Idade_homem_mais_velho = 0

for c in range(1 , 5):
    print(f"==={c} Pessoa===")
    
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    idade1.append(idade)
    sexo = str(input("Sexo: "))
    
    if idade < 20 and sexo == "F":
        mulheres_Menos_De_Vinte += 1

print(f"A Média De Idade Do Grupo é {sum(idade1)/len(idade1)}\nMulheres Com Menos De 20 Anos: {mulheres_Menos_De_Vinte}")
