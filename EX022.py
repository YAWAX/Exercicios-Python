Nome = str(input("Digite seu nome completo: ")).strip()

print(f"Seu nome em maisculo é {Nome.upper()}")
print(f"Seu nome em minusculo é {Nome.lower()}")
print(f"Seu nome tem {len(Nome) - Nome.count(' ')} letras")
#print("Seu primeiro nome tem {} letras".format(Nome.find(' ')))
separa = Nome.split()
print("Seu primeiro nome é {} e tem {} ".format(separa[0] , len(separa[0])))
