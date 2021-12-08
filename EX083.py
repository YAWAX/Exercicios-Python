"""Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use 
parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

###########PRINCIPAL####################
expressão = '((a+b)*c)(x+y(3+2/3)*z)'
aberto = fechando = 0

for c in expressão:
    if c == '(':
        aberto += 1

    elif c == ')':
        fechando += 1
    
print("Expressão Valida" if aberto == fechando else "Expressão Invalida")
