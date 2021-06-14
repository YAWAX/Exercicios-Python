#Exercício Python #038 - Comparando números

'''
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais


'''

Numero1 = input("Digite um valor numérico\033[0;32;40m ")
Numero2 = input("\033[m Digite um valor numérico\033[0;32;40m:  ")
Validar = Numero1.isnumeric()
Validar1 = Numero2.isnumeric()

## DA LINHA 19 ATE A LINHA 33 EO CODIGO DE VALIDAÇÃO PARA SABER SE OS NUMEROS DIGITAS SÃO NUMEROS INTEIROS

if Validar != True:
    while True:
        print("\033[0;31;40mO valor deve ser um numero inteiro\033[m")
        
        Numero1 = input("Digite um valor numérico:")
        Numero2 = input("Digite um valor numérico:  ")
        break

if Validar1 != True:
    while True:
        print("\033[0;31;40mO valor deve ser um numero inteiro\033[m")
        
        Numero1 = input("Digite um valor numérico:")
        Numero2 = input("Digite um valor numérico:  ")
        break

if Numero1 > Numero2:
    print(f"O {Numero1} é Maior que o {Numero2}")

elif Numero1 < Numero2:
    print(f"O {Numero2} é Maior que o {Numero1}")

elif Numero1 == Numero2:
    print(f"Os Valores {Numero1} e {Numero2} são iguais")

else:
    print("OPS ALGO DEU ERRADO SAI E ENTRE NOVAMENTE NO PROGRAMA")

print("Obrigado por usar o programa do Rem ATÉ MAIS")

#FIM
