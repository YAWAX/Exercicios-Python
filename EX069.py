pessoas18anos = 0
homens_CADASTRADOS = 0
Mulheres_Menos_De_20 = 0

while True:
    print("\n=========CADASTRO DE PESSOAS=========")
    
    idade = int(input("\nDigite A Idade: "))    
    if idade >= 18:
        pessoas18anos += 1

    sexo = str(input("Escreva O Sexo: ")).upper()[0]
    
    if sexo == 'M':
        homens_CADASTRADOS += 1
    
    while sexo not in 'MF':       
        sexo = str(input("Escreva O Sexo: ")).upper()[0]
        if sexo == 'M':
            homens_CADASTRADOS += 1

    if idade < 20 and sexo == 'F':
        Mulheres_Menos_De_20 += 1
    
    print("===PESSOA CADASTRADA COM SUCESSO===\n")
    
    sair = str(input("Deseja Continuar: ")).upper()[0]    
    while sair not in 'SN':
        sair = str(input("Deseja Continuar: ")).upper()[0]

    if sair == 'N':
        break

print(f"""\n=========FINALIZADO=========\nTotal De Pessoa Com Mais De 18 anos: {pessoas18anos}
Ao Todo Temos {homens_CADASTRADOS} homens cadastrados
E Temos {Mulheres_Menos_De_20} mulher Com Menos De 20 Anos\n""")
