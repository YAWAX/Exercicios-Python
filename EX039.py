#Exercício Python #039 - Alistamento Militar

from datetime import date

ANOATUAL = date.today().year
Ano1 = int(input("Digite seu ano de nascimento: "))
IDADE = ANOATUAL - Ano1
print(f"Quem nasceu em {Ano1} tem hoje {IDADE} anos de idade")

if IDADE < 18:
    ANOS_FALTAM = IDADE - 18
    print(f'\033[0;32;40mfaltam {0 - ANOS_FALTAM} anos para o alistamento\nSeu alistamento sera em {0 - (ANOS_FALTAM - ANOATUAL)}\033[m')

elif IDADE == 18:
    print("\033[0;32;40mVocê precisa se alistar,se ja o fez aguarde orientação\033[m")

elif IDADE > 18:
    print("\033[0;31;40mVocê ja deveria ter se alistado,se nao o fez procure informação na junta\n militar mais proxima\033[m")
