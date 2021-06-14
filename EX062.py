print('=' * 25)
print("10 TERMOS DE UMA PA")
print('=' * 25 )

a1 = int(input("PRIMEIRO TERMO: "))
r = int(input("Razão: "))
termo = a1
cont = 1
mais = 10
total = 0
op = 0

while op != 3:
    total = total + mais

    while cont <= total:
        print(termo, end=" x ")
        termo += r
        cont += 1

    op = int(input("""\n[1]Quantos Termos Quer Ver A Mais:
[2]Limpar PA/ 10 Primeiros Termos
[3]Sair
>>>>> """))
    if op == 1:
        mais = int(input("Quantos Termos Você Quer Ver A Mais: "))

    elif op == 2:
        a1 = int(input("PRIMEIRO TERMO: "))  
        r = int(input("Razão: "))  

    elif op == 3:
        print(f"Progressão Finalizada Com {total} termos Mostrados")

    else:
        print("Valor Invalido Tente Novamente.")        
