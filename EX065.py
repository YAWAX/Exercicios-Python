"""
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

sair = "S"
cont = soma = maior = menor = 0

while sair in 'Ss':
    n1 = int(input("Digite Um Número Inteiro: "))
    cont += 1 
    soma += n1
    sair = str(input("Deseja Continuar: ")).upper()
    if cont == 1:
        maior = menor = n1
    
    else:
        if n1 > maior:
            maior = n1
        
        if n1 < menor:
            menor = n1
print(f"Você Digitou {cont} Números\nA Média Dos Valores Digitados é {soma / cont}\nO Maior Valor é {maior} e o Menor é {menor}")
