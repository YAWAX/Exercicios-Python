nome = str(input("Digite uma frase: ")).upper().strip()
x = nome.count('A')
print(f'A letra (A) aparece {x} vezes na frase\nA primeira letra A aparceu na posição {nome.find("A")+1}')
print(f"A Letra A apareceu por ultimo na poisção {nome.rfind('A')+1 }")

