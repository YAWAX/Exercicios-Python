#Exercício Python #015 - Aluguel de Carros

dias_alugados = int(input("Quantos dias foi alugado : "))#####PERGUNTA
km_rodados = float(input("Quantos km rodados: "))######PERGUNTA

valor_por_dia = dias_alugados * 60 ######Calculo
km_preco = km_rodados * 0.15 ######Calculo
total = valor_por_dia + km_preco ######Calculo 

print(f"O tatal a pagar é de {total}")
