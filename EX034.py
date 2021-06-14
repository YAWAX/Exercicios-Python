import time
S1  = float(input("Qual o valor do funcionario R$: "))

if S1 <= 1250:
    aumento = S1 + (S1 * 15 / 100)

else:
    aumento = S1 + (S1 * 10 / 100)


print(f"Seu novo salario é {aumento}")
