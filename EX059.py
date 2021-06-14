"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

N1 = int(input("\nDigite Um Valor Inteiro: "))
N2 = int(input("Digite Um Valor Inteiro: "))

OP = 0

while OP != 5:
    OP = int(input("""\nEscolha Uma Das Opções Abaixo:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
>>>>>>>>> Qual A Sua Opção? """))

    if OP == 1:
        print(f"\nA Soma Entre {N1} x {N2} = {N1 + N2}")
    
    if OP == 2:
        print(f"\nA Multiplicação Entre {N1} x {N2} = {N1 * N2}")
        
    if OP == 3:
        if N1 > N2:
            print(f"\nO Maior Valor entre {N1} e {N2} é {N1}")
        elif N1 < N2:
            print(f"\nO Maior Valor entre {N1} e {N2} é {N2}")
        elif N1 == N2:
            print("Os Valores {N1} e {N2} São Iguais")

    if OP == 4:
        print("\nDigite Novos Valores: ")
        N1 = int(input("Digite Um Valor Inteiro: "))
        N2 = int(input("Digite Um Valor Inteiro: "))

    if OP == 5:
        print("FINALIZANDO...")
        break

    else:
        print("Valor Invalido, Digite Novamente")

print("VOLTE SEMPRE")
