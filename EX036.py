Valor_casa = float(input("Valor da Casa: "))
salario_comprador = float(input("Seu Salario: "))
Anos = int(input("Quantos anos quer pagar: "))

Mês = Anos * 12
Minimo = salario_comprador * 30 /100
Prestação_Mensal = Valor_casa / Mês 
print(Prestação_Mensal)

if Prestação_Mensal > salario_comprador:
    print("Seu Salario Não é suficiente: ")

elif Prestação_Mensal >= Minimo:
    print("NEGADO")

else:
    Prestação_Mensal < Minimo
    print("CONCEDIDO")
