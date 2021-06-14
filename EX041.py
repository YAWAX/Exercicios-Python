#Python Exercício #041 - Classificando Atletas

'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

import datetime


Ano_DE_Nascimento = int(input('Digite seu ano de nascimento: '))
Ano123 = datetime.date.today().year
IDADE  = Ano123 - Ano_DE_Nascimento
print(IDADE)

print(f"O Atleta tem {IDADE} anos")


if IDADE == 9:
    print("Classificação mirim")

elif IDADE < 9:
    print("A criança tem que ter mais de 9 anos")

elif IDADE > 9 and IDADE < 14 :
    print("Classificação Infatil")

elif IDADE > 14 and IDADE < 19 :
    print("Classificação junior")

elif IDADE >19 and IDADE < 25 :
    print("Classificalçao Sênior")

elif IDADE > 25:
    print("Classificação Master")

else:
    print("Algo deu errado,tente de novo")
