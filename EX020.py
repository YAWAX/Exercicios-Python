from random import choices

quantas_pessoas = int(input("Quantaas pessoas ; "))
n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno ")
n3 = input("Terceiro aluno ")
n4 = input("Quarto aluno: ")
lista = [n1 , n2 ,n3 , n4]
escolha = choices(lista , k=quantas_pessoas) # k = 2 serão escolhidos 2 dentre os 4 alunos
print(escolha)
