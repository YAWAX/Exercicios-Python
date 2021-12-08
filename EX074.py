import random

n1 = random.randint(0, 10)    
n2 = random.randint(0, 10)
n3 = random.randint(0, 10)
n4 = random.randint(0, 10)
n5 = random.randint(0, 10)

tupla = (n1, n2, n3, n4, n5)
print(f"Números Gerados: {tupla}\nMaior: {max(tupla)}\nMenor: {min(tupla)}")
