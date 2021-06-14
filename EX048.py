soma = 0
contador = 0

for c in range(1 , 501 , 2):
    if c % 3 ==0:
        contador += 1
        soma += c

print(f"A SOMA DE TODOS {contador} OS VALORES SOLICITADOS É {soma}")
