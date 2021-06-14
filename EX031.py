#Exercício Python #031 - Custo da Viagem

Distancia = float(input("Digite a distância da sua viagem: "))


if Distancia < 199:
    ValorDaPassagem = Distancia * 0.50
    print(f"O preço d viagem é de {ValorDaPassagem}")

else:
    ValorDaPassagem = Distancia * 0.45
    print(f"O preço da viagem é de {ValorDaPassagem}")

