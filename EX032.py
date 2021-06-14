#Exercício Python #032 - Ano Bissexto
import datetime

while True:

    Ano = int(input("Digite um ano qualquer: "))

    if Ano == 0:
        Ano123 = datetime.date.today().day

    if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0 :

        print(f"O ano {Ano} é bissexto")

    else:
        print(f"O ano {Ano} não é bissexto")



'''Para ser bissexto, o ano deve ser:

Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;

Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;

Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.'''
