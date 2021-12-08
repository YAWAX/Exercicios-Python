"""Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O 
programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """

total = maior = menor = maisDEMIl = 0
produtoMAISBarato = ''
produtoMAISCaro = ''

while True:
    produto = str(input("Nome Do Produto: "))
    preço = float(input(f"Preço do/a {produto}: "))
    total += preço
    
    if total == preço:
        maior = menor = preço
        produtoMAISBarato = produto

    else:
        if preço > maior:
            maior = preço
            produtoMAISCaro = produto
    
        if preço < menor:
            menor = preço
            produtoMAISBarato = produto

    if preço > 1000:
        maisDEMIl += 1

    sair = str(input("Deseja Sair? ")).upper()[0]
    if sair == 'S':
        break

print("============FINALIZADO============")
print(f"\nO Total Gasto foi de {total}\nProdutos Com Valor Superior A mil reais {maisDEMIl}\nO PRoduto Mais Barato foi de {produtoMAISBarato} com Valor De {menor}\nO Produto Mais Caro Foi {produtoMAISCaro} Com Valor De R${maior}")
