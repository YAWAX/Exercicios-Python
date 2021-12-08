numeros = [[], []]
for c in range(0 , 7):
    Valor = int(input("Valor: "))   
    
    if Valor % 2 == 0:
        numeros[0].append(Valor) 

    else:
        numeros[1].append(Valor)

print('——'*20)
numeros[0].sort()
numeros[1].sort()
print(f"Os Valores Pares Digitadis Foram: {numeros[0]}")
print(f"Os Valores Impares Digitados Foram: {numeros[1]}")
print('——'*20)
