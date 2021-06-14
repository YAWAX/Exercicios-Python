N1I = int(input("Digite um numero inteiro: "))
u = N1I // 1 % 10
d = N1I // 10 % 10
c = N1I // 100 % 10
m = N1I // 1000 % 10

print(f"{u} Unidades")
print(f"{d} Dezenas")
print(f"{c} Centena")
print(f"{m} Milhar")
