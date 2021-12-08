numeros = []
while True:
    if len(numeros) == 5:
        break
    numeros.append(int(input("Valor: ")))


Maior = numeros.count(max(numeros))


print(f"Valores Digitados: {numeros}")
print(f"O Maior Valor Da Sequência é {max(numeros)} Na Posição {numeros.index(max(numeros))+1}")
print(f"O Menor Valor Da Sequência é {min(numeros)} Na Posição {numeros.index(min(numeros))+1}")
