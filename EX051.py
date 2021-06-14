#Exercício Python #051 - Progressão Aritmética

print('=' * 25)
print("10 TERMOS DE UMA PA")
print('=' * 25 )

a1 = int(input("PRIMEIRO TERMO: "))  #termo
r = int(input("Razão: "))  #razâo
decimo = a1 + (10 -1 )*r

for c in range(a1 , decimo + r , r):
    print(f' {c} ' ,end='=' )

print("ACABOU")
