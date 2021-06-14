#Exercício Python #030 - Par ou Ímpar?

    
while True:
    Numero = int(input("Digite um numero qualquer: "))
    par = Numero % 2
    if par == 0:
        print(f"\033[0;33;40m{Numero} é par\033[m")
    else:
        print(f"\033[0;32;40m{Numero} é impar\033[m ")
