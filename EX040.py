#Exercício Python #040 - Aquele clássico da Média

'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
 mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

nota1 = float(input("Nota 1 : "))
nota2 = float(input("Nota 2 : "))

media = (nota1 + nota2) / 2

messagemreprovado = 'Você Esta Reprovado!'
mensagemrecuperação = 'Você esta de recuperação!'
mensagemAprovado = 'Você esta aprovado!'

if media <= 5.0:
    print("A sua media é {}, você esta {}".format(media , messagemreprovado))

elif media >= 5.0 and media <= 7:
    print('A sua media é {}, voce esta {}'.format(media , mensagemrecuperação))


elif media >= 7.0 and media < 10:
    print('A sua media é {}, voce esta {}'.format(media , mensagemAprovado))

else:
    print(f' Algo deu errado,tente de novo ')
