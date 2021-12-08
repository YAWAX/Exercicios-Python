Aluno = dict()

Aluno['nome'] = str(input("Nome Do Aluno: "))
Aluno['media'] = float(input("Media: "))

if Aluno["media"] >=7:
    Aluno['situação'] = 'Aprovado'

elif Aluno["media"] >=5 and Aluno['media'] < 7:
    Aluno['situação'] = 'Recuperação'

else:
    Aluno['situação'] = 'Reprovado'

print()
for k, v in Aluno.items():
    print(f"  - {k} é igual a {v}")
