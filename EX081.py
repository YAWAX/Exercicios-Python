lista = []
while True:
    n = int(input("Valor: "))
    lista.append(n)
    
    #sair = str(input("Deseja Continuar: ")).upper()
    if len(lista) == 5:
        break

print(f"\nForam Digitados: {len(lista)} Valores")
lista.sort(reverse=True)
print(f"Os Valores em ordem decrescente são {lista}")
print("O Valor 5 faz parte da lista\n"if 5 in lista else "O Valor 5 Nao faz parte da lista\n")
