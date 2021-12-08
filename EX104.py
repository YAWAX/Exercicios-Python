def leiaInt(Inteiro):

    Inteiro = input('Número: ')

    if Inteiro.isdigit() == True:
        return Inteiro

    else:
        while True:
            print("ERRO! Digite Um Número Inteiro Valido")
            Inteiro = input('Número: ')

            if Inteiro.isdigit() == True:
                return Inteiro


n = leiaInt("Número: ")
print(f"Você Acabou De Digitar o Número {n}")
