p1 = float(input("Qual o preço do produto? R$ "))
desconto = p1 - 5/100 * p1 
print("O produto que custava {}, na promoção com desconto de 5% vais custar {:.2f}".format(p1 , desconto))
