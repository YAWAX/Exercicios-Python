n1 = int(input("Digite um numero inteiro: "))
print("""Escolha uma base para converter 
1 binario
2 octal
3 hexa""")
opçao = int(input("OPÇâo "))
if opçao == 1:
    print(n1,bin(n1))

elif opçao == 2:
    print(n1,oct(n1))

else:
    print(n1,hex(n1))
    