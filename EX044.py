#Exercício Python #044 - Gerenciador de Pagamentos

'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print('='*25,'LOJAS DO REM', '='*25)
preco_DAS_compras = float(input("Preço das compras: R$ "))
print('''[1] à vista dinheiro/cheque:\n[2]à vista no cartão:\n[3]2x no cartão:\n[4]3x ou mais no cartão''')
PAGAMENTO = int(input("QUAL A FORMA DE PAGAMENTO: "))

if PAGAMENTO == 1:
    desconto = preco_DAS_compras - (10/100 * preco_DAS_compras)
    print(f"Sua compra de {preco_DAS_compras} vai custar {desconto} no final")

if PAGAMENTO == 2:
    desconto = preco_DAS_compras - (5/100 * preco_DAS_compras)
    print(f"Sua compra de {preco_DAS_compras} vai custar {desconto} no final ")

if PAGAMENTO == 3:
    desconto = preco_DAS_compras
    parcelado = preco_DAS_compras / 2
    print(f"Sua compra de {preco_DAS_compras} parcelada em 2 vezes, R${parcelado} por mês sem juros")

if PAGAMENTO == 4:
    parcelas = int(input("QUANTAS PARCELAS SEU POBRE: "))
    TOTALPARCELADO = preco_DAS_compras / parcelas
    desconto = preco_DAS_compras + (20/100 * preco_DAS_compras)
    print(f"Sua compra de {preco_DAS_compras} parcela em {parcelas}, vai ficar {TOTALPARCELADO} por mês,com juros de 20%.TOTAL NO FINAL VAI SER:{ desconto }")
