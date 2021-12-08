numeros = ('Um',  'Dois' , 'Três', 'Quatro', 'Cinco', "Seis", 'Sete', "Oito", "Nove", "Dez", 'Onze', "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezesete", "Dezoito", "Dezenove", "Vinte")
n1 = int(input("Digite Um Valor Inteiro De Um Até Vinte: "))
while True:
    if n1 < 1 or n1 > 20:
        print("Valor Invalido")
        n1 = int(input("Digite Um Valor Inteiro De Um Até Vinte: "))
    else:
        break
print(numeros[n1-1])
